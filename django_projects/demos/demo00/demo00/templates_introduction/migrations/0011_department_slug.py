# Generated by Django 4.1.1 on 2022-10-08 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templates_introduction', '0010_alter_company_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
