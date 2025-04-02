from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password


class UserModelManager(BaseUserManager):
    """Foydalanuvchilarni yaratish uchun manager"""

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email kiritish majburiy!")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Parolni hash qilish
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Superuser yaratish"""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class UserModel(AbstractBaseUser, PermissionsMixin):
    """Custom User modeli - Email orqali autentifikatsiya qilish"""

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, unique=True, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)
    latitude = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"  # Email orqali autentifikatsiya
    REQUIRED_FIELDS = []

    objects = UserModelManager()

    def __str__(self):
        return self.email


    def __str__(self):
        return self.username
      
    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
    
    def check_password(self, raw_password):
        """
        Check if the raw_password matches the hashed password
        """
        return check_password(raw_password, self.password)
      
    def check_password(self, raw_password):
      from django.contrib.auth.hashers import check_password
      return check_password(raw_password, self.password)
