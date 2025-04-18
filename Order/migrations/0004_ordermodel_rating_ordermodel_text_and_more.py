# Generated by Django 5.1.7 on 2025-04-01 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0003_alter_ordermodel_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
