from django.db import models
from django.utils import timezone
from ProductApp.models import Product
from CategoryApp.models import Category

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sales')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sales')
    discount = models.PositiveIntegerField()  # Foizda (1-100)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.product.name} - {self.discount}%"
    
    def save(self, *args, **kwargs):
        # Chegirma muddati tugagan bo'lsa, avtomatik o'chirish
        if self.end_date < timezone.now():
            self.is_active = False
        super().save(*args, **kwargs)