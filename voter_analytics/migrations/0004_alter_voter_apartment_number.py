# Generated by Django 5.1.2 on 2024-11-08 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voter_analytics', '0003_alter_voter_v20state_alter_voter_v21primary_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='apartment_number',
            field=models.IntegerField(blank=True),
        ),
    ]
