# Generated by Django 4.1.2 on 2022-10-08 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_autocomplete_slug_in_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='slug',
            field=models.SlugField(default='none', unique=True),
            preserve_default=False,
        ),
    ]