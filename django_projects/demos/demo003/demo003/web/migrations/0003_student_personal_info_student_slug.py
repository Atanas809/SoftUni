# Generated by Django 4.1.2 on 2022-10-14 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_student_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='personal_info',
            field=models.PositiveIntegerField(max_length=10, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='student',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
