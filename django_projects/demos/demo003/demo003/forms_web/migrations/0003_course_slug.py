# Generated by Django 4.1.2 on 2022-10-15 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms_web', '0002_alter_company_options_alter_course_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
