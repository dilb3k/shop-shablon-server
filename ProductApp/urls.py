from django.urls import path
from .views import ProductListCreateAPI, ProductDetailAPI, ProductImageUploadAPI

urlpatterns = [
    path('products/', ProductListCreateAPI.as_view(), name='product-list'),
    path('products/<int:id>/', ProductDetailAPI.as_view(), name='product-detail'),  # uuid -> int
    path('products/<int:product_id>/upload-image/', ProductImageUploadAPI.as_view(), name='product-image-upload'),
]

