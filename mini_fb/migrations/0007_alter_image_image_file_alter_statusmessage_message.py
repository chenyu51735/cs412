# Generated by Django 5.1.2 on 2024-10-21 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0006_alter_image_image_file_alter_image_status_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_file',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='statusmessage',
            name='message',
            field=models.TextField(blank=True),
        ),
    ]