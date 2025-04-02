from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ChatRoom, Message
from .serializers import ChatRoomSerializer, MessageSerializer, MessageCreateSerializer
from django.db.models import Q

class ChatRoomListCreateAPI(generics.ListCreateAPIView):
    serializer_class = ChatRoomSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return ChatRoom.objects.filter(participants=self.request.user)
    
    def perform_create(self, serializer):
        chat_room = serializer.save()
        chat_room.participants.add(self.request.user)

class ChatRoomDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChatRoomSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return ChatRoom.objects.filter(participants=self.request.user)

class MessageListAPI(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        room_id = self.kwargs.get('room_id')
        return Message.objects.filter(
            room_id=room_id,
            room__participants=self.request.user
        ).order_by('-timestamp')

class MessageCreateAPI(generics.CreateAPIView):
    serializer_class = MessageCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        room = serializer.validated_data['room']
        if self.request.user not in room.participants.all():
            return Response(
                {"error": "You are not a participant in this chat room"},
                status=status.HTTP_403_FORBIDDEN
            )
        serializer.save(sender=self.request.user)

class MessageMarkAsReadAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, message_id):
        try:
            message = Message.objects.get(
                id=message_id,
                room__participants=request.user
            )
            if not message.read:
                message.read = True
                message.save()
            return Response({"status": "success"})
        except Message.DoesNotExist:
            return Response(
                {"error": "Message not found"},
                status=status.HTTP_404_NOT_FOUND
            )

class UnreadMessagesCountAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        count = Message.objects.filter(
            room__participants=request.user,
            read=False
        ).exclude(sender=request.user).count()
        return Response({"unread_count": count})