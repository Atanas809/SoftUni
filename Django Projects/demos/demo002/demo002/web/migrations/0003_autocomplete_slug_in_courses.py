# Generated by Django 4.1.2 on 2022-10-10 13:10

from django.db import migrations
from django.utils.text import slugify


def add_slug(apps, schema_editor):
    Course = apps.get_model('web', 'Course')

    courses = Course.objects.all()

    for course in courses:
        course.slug = slugify(course.name)

    Course.objects.bulk_update(courses, ['slug'])


def delete_slug(apps, schema_editor):
    Course = apps.get_model('web', 'Course')

    courses = Course.objects.all()

    for course in courses:
        course.slug = None

    Course.objects.bulk_update(courses, ['slug'])


class Migration(migrations.Migration):
    dependencies = [
        ('web', '0002_course_slug'),
    ]

    operations = [
        migrations.RunPython(add_slug, delete_slug)
    ]