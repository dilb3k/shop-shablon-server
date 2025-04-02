from rest_framework import serializers
from .models import Sale
from ProductApp.models import Product
from ProductApp.serializers import ProductSerializer
from django.utils import timezone

class DiscountedProductSerializer(ProductSerializer):
    discount_info = serializers.SerializerMethodField()
    final_price = serializers.SerializerMethodField()

    class Meta(ProductSerializer.Meta):
        fields = ProductSerializer.Meta.fields + ['discount_info', 'final_price']
    
    def get_discount_info(self, obj):
        active_sale = obj.sales.filter(
            start_date__lte=timezone.now(),
            end_date__gte=timezone.now()
        ).first()
        
        if active_sale:
            return {
                'discount_percentage': active_sale.discount,
                'start_date': active_sale.start_date,
                'end_date': active_sale.end_date
            }
        return None
    
    def get_final_price(self, obj):
        active_sale = obj.sales.filter(
            start_date__lte=timezone.now(),
            end_date__gte=timezone.now()
        ).first()
        
        if active_sale:
            return obj.price * (100 - active_sale.discount) / 100
        return obj.price

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'

from rest_framework import serializers
from ProductApp.models import Product
from ProductApp.serializers import ProductSerializer
from django.utils import timezone

class SaleProductSerializer(ProductSerializer):
    discount_percentage = serializers.SerializerMethodField()
    discounted_price = serializers.SerializerMethodField()
    sale_end_date = serializers.SerializerMethodField()

    class Meta(ProductSerializer.Meta):
        fields = ProductSerializer.Meta.fields + [
            'discount_percentage', 
            'discounted_price',
            'sale_end_date'
        ]
    
    def get_discount_percentage(self, obj):
        active_sale = obj.sales.filter(
            start_date__lte=timezone.now(),
            end_date__gte=timezone.now()
        ).first()
        return active_sale.discount if active_sale else None
    
    def get_discounted_price(self, obj):
        active_sale = obj.sales.filter(
            start_date__lte=timezone.now(),
            end_date__gte=timezone.now()
        ).first()
        if active_sale:
            return obj.price * (100 - active_sale.discount) / 100
        return obj.price
    
    def get_sale_end_date(self, obj):
        active_sale = obj.sales.filter(
            start_date__lte=timezone.now(),
            end_date__gte=timezone.now()
        ).first()
        return active_sale.end_date if active_sale else None