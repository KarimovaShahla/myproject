# Generated by Django 5.0.6 on 2024-09-15 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0007_category_super_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertyimage',
            name='order',
            field=models.SmallIntegerField(default=0),
        ),
    ]
