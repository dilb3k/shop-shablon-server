from django.urls import path
from .views import SaleListCreateAPI, CategorySaleProductsAPI, DiscountedProductsByCategoryView

urlpatterns = [
    path('sale/', SaleListCreateAPI.as_view(), name='sale-list-create'),
    path('category-discounts/<slug:slug>/', DiscountedProductsByCategoryView.as_view(), name='discounted-products-by-category'),
    path('sale/<slug:slug>/', CategorySaleProductsAPI.as_view(), name='category-sale-products'),
]