# Generated by Django 4.1.2 on 2022-10-09 09:32

from django.db import migrations
from django.utils.text import slugify


def add_slug(apps, schema_editor):
    City = apps.get_model('web', 'City')

    cities = City.objects.all()

    for city in cities:
        city.slug = slugify(city.postal_code)

    City.objects.bulk_update(cities, ['slug'])


def delete_slug(apps, schema_editor):
    City = apps.get_model('web', 'City')

    cities = City.objects.all()

    for city in cities:
        city.slug = None

    City.objects.bulk_update(cities, ['slug'])


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_city_slug'),
    ]

    operations = [
        migrations.RunPython(add_slug, delete_slug)
    ]
