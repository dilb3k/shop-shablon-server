from django.urls import path
from .views import (
    UserListCreateAPI, UserDetailAPI,
    MyTokenObtainPairView, RegisterAPI, LoginAPI, ProtectedAPI
)

urlpatterns = [
    path('users/', UserListCreateAPI.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailAPI.as_view(), name='user-detail'),
    
    # Auth endpoints
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    
    # Protected endpoint example
    path('protected/', ProtectedAPI.as_view(), name='protected'),
]



