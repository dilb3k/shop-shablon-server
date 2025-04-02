from django.urls import path
from .views import AdminUserListCreateView, AdminUserDetailView, AdminUserLoginView

urlpatterns = [
    path('admin-users/', AdminUserListCreateView.as_view(), name='admin-user-list'),
    path('admin-users/<int:pk>/', AdminUserDetailView.as_view(), name='admin-user-detail'),
    path('admin-login/', AdminUserLoginView.as_view(), name='admin-user-login'),
]
