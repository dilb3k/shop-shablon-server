from django.db import models

from django.contrib.auth import get_user_model

class CartModel(models.Model):
    user_id = models.IntegerField()  # Mahsulot ID
    product_id = models.IntegerField()  # Mahsulot ID
    quantity = models.IntegerField()  # Buyurtma miqdori
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Narx
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)  # Umumiy summa
    order_date = models.DateTimeField(auto_now_add=True)  # Buyurtma sanasi
    status = models.CharField(max_length=20, choices=[
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled')
    ], default='Processing')  # Buyurtma holati

    def __str__(self):
        return f"Cart {self.id} - User {self.user.username}"
