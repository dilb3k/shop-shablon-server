from django.urls import path
from .views import CommentListCreateAPI, CommentDetailAPI, ProductCommentsAPI

urlpatterns = [
    path('comment/', CommentListCreateAPI.as_view(), name='comment-list-create'),
    path('comment/<int:pk>/', CommentDetailAPI.as_view(), name='comment-detail'),
    path('product/<str:product_id>/', ProductCommentsAPI.as_view(), name='product-comments'),
]