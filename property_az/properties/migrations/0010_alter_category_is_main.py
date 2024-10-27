# Generated by Django 5.0.6 on 2024-09-17 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0009_property_expires_at_property_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='is_main',
            field=models.BooleanField(blank=True, choices=[(False, 'NO'), (True, 'YES'), (None, 'UNKNOWN')], default=False, null=True),
        ),
    ]
