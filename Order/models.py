from django.db import models
from Usersapp.models import UserModel  

# models.py
class OrderModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    product_id = models.CharField(max_length=1000)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled')
    ], default='Processing')
    text = models.TextField(blank=True, null=True)  # Yangi qo'shilgan maydon
    rating = models.IntegerField(blank=True, null=True)  # Yangi qo'shilgan maydon

    def __str__(self):
        return f"Order {self.id} - User {self.user.username}"