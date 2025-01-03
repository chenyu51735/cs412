# Generated by Django 5.1.2 on 2024-10-22 20:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0007_alter_image_image_file_alter_statusmessage_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('profile1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile1', to='mini_fb.profile')),
                ('profile2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile2', to='mini_fb.profile')),
            ],
        ),
    ]
