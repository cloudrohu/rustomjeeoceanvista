# Generated by Django 5.0.2 on 2025-05-03 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_location_maharera_alter_bookingopen_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='mobile_image',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='section',
        ),
    ]
