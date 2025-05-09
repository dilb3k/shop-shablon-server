# Generated by Django 5.1.7 on 2025-03-30 11:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ProductApp', '0001_initial'),
        ('Usersapp', '0003_alter_usermodel_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProductApp.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usersapp.usermodel')),
            ],
        ),
    ]
