# Generated by Django 4.1.2 on 2022-10-08 11:14

from django.db import migrations
from django.utils.text import slugify


def add_slug(apps, scheme_editor):
    Student = apps.get_model('web', 'Student')

    students = Student.objects.all()

    for student in students:
        student.slug = slugify(student.last_name)

    Student.objects.bulk_update(students, ['slug'])


def delete_slug(apps, scheme_editor):
    Student = apps.get_model('web', 'Student')

    students = Student.objects.all()

    for student in students:
        student.slug = None

    Student.objects.bulk_update(students, ['slug'])


class Migration(migrations.Migration):
    dependencies = [
        ('web', '0006_student_slug'),
    ]

    operations = [
        migrations.RunPython(add_slug, delete_slug)
    ]
