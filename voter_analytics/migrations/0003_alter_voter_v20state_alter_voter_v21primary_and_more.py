# Generated by Django 5.1.2 on 2024-11-08 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voter_analytics', '0002_rename_date_of_registeration_voter_date_of_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='v20state',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='voter',
            name='v21primary',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='voter',
            name='v21town',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='voter',
            name='v22general',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='voter',
            name='v23town',
            field=models.TextField(),
        ),
    ]
