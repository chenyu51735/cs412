# Generated by Django 5.1.1 on 2024-10-08 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='auther',
            new_name='author',
        ),
    ]
