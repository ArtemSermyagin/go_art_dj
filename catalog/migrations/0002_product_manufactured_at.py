# Generated by Django 5.0.2 on 2024-02-23 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='manufactured_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата производства продукта'),
        ),
    ]
