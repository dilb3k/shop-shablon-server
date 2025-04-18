from django.db import models
from django.utils import timezone
from ProductApp.models import Product
from CategoryApp.models import Category

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sales')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sales')
    discount = models.PositiveIntegerField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.product.name} - {self.discount}%"
    
    def save(self, *args, **kwargs):
     now = timezone.now()
     self.is_active = self.start_date <= now < self.end_date  
     super().save(*args, **kwargs)

    
    @classmethod
    def get_active_sales(cls):
        """Returns only currently active sales"""
        now = timezone.now()
        return cls.objects.filter(
            start_date__lte=now,
            end_date__gte=now,
            is_active=True
        )