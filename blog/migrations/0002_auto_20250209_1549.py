# Generated by Django 3.2.8 on 2025-02-09 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='busFare',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='schedule',
            name='seatsRemaining',
            field=models.IntegerField(default=0),
        ),
    ]
