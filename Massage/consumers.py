import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from .models import ChatRoom, Message

User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = f'chat_{self.room_id}'
        
        # Autentifikatsiyani tekshirish
        if not self.scope["user"].is_authenticated:
            await self.close()
            return
            
        # Xonaga ulanish
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Xonadan chiqish
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
        # Xabarni bazaga saqlash
        await self.save_message(self.scope["user"], message)
        
        # Xabarni guruhga yuborish
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender_id': self.scope["user"].id,
                'sender_username': self.scope["user"].username,
                'timestamp': str(self.scope["timestamp"])
            }
        )

    async def chat_message(self, event):
        # Xabarni websocket orqali yuborish
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'sender_id': event['sender_id'],
            'sender_username': event['sender_username'],
            'timestamp': event['timestamp']
        }))

    @database_sync_to_async
    def save_message(self, user, content):
        room = ChatRoom.objects.get(id=self.room_id)
        Message.objects.create(room=room, sender=user, content=content)