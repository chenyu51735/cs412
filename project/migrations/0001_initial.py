# Generated by Django 5.1.3 on 2024-11-19 04:30

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
                ('rating', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
