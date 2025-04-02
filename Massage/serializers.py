from rest_framework import serializers
from .models import ChatRoom, Message
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ChatRoomSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    participant_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.all(),
        write_only=True,
        source='participants'
    )
    
    class Meta:
        model = ChatRoom
        fields = ['id', 'name', 'participants', 'participant_ids', 'created_at', 'updated_at', 'is_group']
        read_only_fields = ['id', 'created_at', 'updated_at']

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    room = ChatRoomSerializer(read_only=True)
    room_id = serializers.PrimaryKeyRelatedField(
        queryset=ChatRoom.objects.all(),
        write_only=True,
        source='room'
    )
    
    class Meta:
        model = Message
        fields = ['id', 'room', 'room_id', 'sender', 'content', 'timestamp', 'read']
        read_only_fields = ['id', 'sender', 'timestamp']

class MessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['room', 'content']