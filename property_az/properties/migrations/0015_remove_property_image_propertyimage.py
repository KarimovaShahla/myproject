# Generated by Django 5.1.1 on 2024-10-08 18:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0014_property_image_delete_propertyimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='image',
        ),
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='property_images/%Y/%m/%d/')),
                ('order', models.SmallIntegerField(default=0)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='properties.property')),
            ],
            options={
                'verbose_name': 'Property Image',
                'verbose_name_plural': 'Property Images',
            },
        ),
    ]
