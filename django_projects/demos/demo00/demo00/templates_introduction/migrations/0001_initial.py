# Generated by Django 4.1.1 on 2022-10-05 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('employees', models.PositiveIntegerField()),
                ('month_income', models.DecimalField(decimal_places=5, max_digits=8)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('hiring', models.BooleanField(null=True)),
                ('company_email', models.EmailField(max_length=254)),
                ('awards', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
