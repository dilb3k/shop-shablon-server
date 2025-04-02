from django.urls import path
from .views import BlogListCreateAPI, BlogDetailAPI

urlpatterns = [
    path('blog/', BlogListCreateAPI.as_view(), name='blog-list-create'),
    path('blog/<int:pk>/', BlogDetailAPI.as_view(), name='blog-detail'),
]
