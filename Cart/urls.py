from django.urls import path
from .views import CartListCreateAPI, CartDetailAPI, ClearCartAPI

urlpatterns = [
    path('cart/', CartListCreateAPI.as_view(), name='cart-list-create'),
    path('cart/<int:pk>/', CartDetailAPI.as_view(), name='cart-detail'),
    path('cart/clear/', ClearCartAPI.as_view(), name='clear-cart'),
]
