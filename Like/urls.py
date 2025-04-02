# urls.py
from django.urls import path
from .views import LikeListCreateAPI, LikeDetailAPI, LikeProductView, UnlikeProductView

urlpatterns = [
    path('like/', LikeListCreateAPI.as_view(), name='like-list-create'),
    path('like/<int:pk>/', LikeDetailAPI.as_view(), name='like-detail'),
    path('like-product/', LikeProductView.as_view(), name='like-product'),  
    path('like-product/<int:pk>/', UnlikeProductView.as_view(), name='unlike-product'),
]
