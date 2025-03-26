from django.urls import path
from .views import UserListCreateAPI, UserDetailAPI

urlpatterns = [
    path('users/', UserListCreateAPI.as_view(), name='user-list-create'),
    path('users/<uuid:pk>/', UserDetailAPI.as_view(), name='user-detail'),
]
