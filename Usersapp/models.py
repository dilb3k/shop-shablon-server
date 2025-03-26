from django.db import models
import uuid

class UserModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Hashlash tavsiya qilinadi!
    longitude = models.CharField(max_length=20)
    latitude = models.CharField(max_length=20)
    phone = models.CharField(max_length=20, unique=True)
    otp = models.CharField(max_length=10)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=10, choices=[('user', 'User'), ('admin', 'Admin')], default='user')

    def __str__(self):
        return self.username
