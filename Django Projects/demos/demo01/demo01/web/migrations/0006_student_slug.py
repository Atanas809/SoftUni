# Generated by Django 4.1.2 on 2022-10-08 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_school_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
