# Generated by Django 4.1.1 on 2022-10-05 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templates_introduction', '0004_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('deadline', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='company',
            name='month_income',
            field=models.DecimalField(decimal_places=5, max_digits=8, verbose_name='Monthly income'),
        ),
        migrations.AddField(
            model_name='employee',
            name='projects',
            field=models.ManyToManyField(to='templates_introduction.project'),
        ),
    ]
