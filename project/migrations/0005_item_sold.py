# Generated by Django 5.1.3 on 2024-12-06 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_transaction_buyer_rating_transaction_seller_rating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='sold',
            field=models.BooleanField(default=False),
        ),
    ]
