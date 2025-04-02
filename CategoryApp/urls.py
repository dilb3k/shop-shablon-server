from django.urls import path
from .views import CategoryListCreateAPI, CategoryDetailAPI, SubcategoryListCreateAPI, SubcategoryDetailAPI

urlpatterns = [
    path('categories/', CategoryListCreateAPI.as_view(), name='category-list'),
    path('categories/<uuid:id>/', CategoryDetailAPI.as_view(), name='category-detail'),
    path('subcategories/', SubcategoryListCreateAPI.as_view(), name='subcategory-list'),
    path('subcategories/<uuid:id>/', SubcategoryDetailAPI.as_view(), name='subcategory-detail'),
]
