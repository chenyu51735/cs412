# Generated by Django 5.1.2 on 2024-11-08 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voter_analytics', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voter',
            old_name='date_of_registeration',
            new_name='date_of_registration',
        ),
    ]
