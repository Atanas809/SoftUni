# Generated by Django 4.1.2 on 2022-10-05 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_employees_department_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('deadline', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='employees',
            name='department_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='web.department', verbose_name='Department'),
        ),
        migrations.AddField(
            model_name='employees',
            name='project_id',
            field=models.ManyToManyField(to='web.projects'),
        ),
    ]
