# management/commands/deactivate_expired_sales.py
from django.core.management.base import BaseCommand
from django.utils import timezone
from your_app.models import Sale

class Command(BaseCommand):
    help = 'Deactivates sales that have passed their end date'

    def handle(self, *args, **options):
        now = timezone.now()
        expired_sales = Sale.objects.filter(
            end_date__lt=now,
            is_active=True
        )
        
        count = expired_sales.update(is_active=False)
        
        self.stdout.write(self.style.SUCCESS(f'Deactivated {count} expired sales'))