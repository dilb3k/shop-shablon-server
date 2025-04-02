from django.urls import path
from .views import OrderListCreateAPI, OrderDetailAPI

urlpatterns = [
    path('orders/', OrderListCreateAPI.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetailAPI.as_view(), name='order-detail'),
]
