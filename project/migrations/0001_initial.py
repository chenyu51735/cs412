# Generated by Django 5.1.3 on 2024-11-22 04:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('nick_name', models.TextField(blank=True)),
                ('email', models.TextField()),
                ('phone', models.TextField()),
                ('city', models.TextField(blank=True)),
                ('bio', models.TextField(blank=True)),
                ('image_file', models.ImageField(blank=True, upload_to='')),
                ('rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='project_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('product', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('brand', models.TextField()),
                ('category', models.CharField(choices=[('Electronics', 'Electronics'), ('Home', 'Home'), ('Collectibles', 'Collectibles'), ('Clothing, Shoes & Accessories', 'Clothing, Shoes & Accessories'), ('Sporting Goods', 'Sporting Goods'), ('Jewelry & Watches', 'Jewelry & Watches'), ('Business & Industrial', 'Business & Industrial')], default='Electronics', max_length=50)),
                ('condition', models.CharField(choices=[('New', 'New'), ('Like New', 'Like New'), ('Good', 'Good'), ('Acceptable', 'Acceptable'), ('Poor', 'Poor')], default='New', max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=11)),
                ('images', models.ImageField(upload_to='')),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_seller', to='project.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateTimeField(auto_now=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to='project.profile')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.item')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to='project.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_date', models.DateTimeField(auto_now=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlist_item', to='project.item')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.profile')),
            ],
        ),
    ]
