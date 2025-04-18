# signals.py
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Sale

@receiver(pre_save, sender=Sale)
def update_sale_status(sender, instance, **kwargs):
    now = timezone.now()
    if now >= instance.end_date: 
        instance.is_active = False
    else:
        instance.is_active = True
