# Generated by Django 4.1.2 on 2022-10-15 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms_web', '0004_autocomplete_slug_in_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
    ]
