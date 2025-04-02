from django.urls import path
from .views import (
    ChatRoomListCreateAPI,
    ChatRoomDetailAPI,
    MessageListAPI,
    MessageCreateAPI,
    MessageMarkAsReadAPI,
    UnreadMessagesCountAPI
)

urlpatterns = [
    path('chat-rooms/', ChatRoomListCreateAPI.as_view(), name='chat-room-list'),
    path('chat-rooms/<int:pk>/', ChatRoomDetailAPI.as_view(), name='chat-room-detail'),
    path('chat-rooms/<int:room_id>/messages/', MessageListAPI.as_view(), name='message-list'),
    path('messages/', MessageCreateAPI.as_view(), name='message-create'),
    path('messages/<int:message_id>/mark-as-read/', MessageMarkAsReadAPI.as_view(), name='mark-as-read'),
    path('messages/unread-count/', UnreadMessagesCountAPI.as_view(), name='unread-count'),
]