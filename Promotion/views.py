# views.py
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from CategoryApp.models import Category
from ProductApp.models import Product
from .models import Sale
from .serializers import SaleSerializer, SaleProductSerializer, DiscountedProductSerializer
from django.utils import timezone
from rest_framework.generics import ListAPIView



class DiscountedProductsByCategoryView(ListAPIView):
    serializer_class = DiscountedProductSerializer
    
    def get_queryset(self):
        category_slug = self.kwargs['slug']
        category = get_object_or_404(Category, slug=category_slug)
        
        return Product.objects.filter(
            category=category,
            sales__start_date__lte=timezone.now(),
            sales__end_date__gt=timezone.now(),
            sales__is_active=True
        ).distinct()
    
class SaleListCreateAPI(ListCreateAPIView):
    serializer_class = SaleSerializer
    
    def get_queryset(self):
        now = timezone.now()
        return Sale.objects.filter(
            is_active=True,
            start_date__lte=now,
            end_date__gt=now
        )


class CategorySaleProductsAPI(ListCreateAPIView):
    serializer_class = SaleProductSerializer

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category, slug=slug)
        
        now = timezone.now()
        products = Product.objects.filter(
            category=category,
            sales__is_active=True,
            sales__start_date__lte=now,
            sales__end_date__gte=now
        ).distinct()
        
        return products