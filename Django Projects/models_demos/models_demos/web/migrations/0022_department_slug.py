# Generated by Django 4.1.2 on 2022-10-06 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0021_alter_category_options_alter_employees_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
