# Generated by Django 2.2.1 on 2019-05-23 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0014_auto_20190523_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos',
            name='slug',
            field=models.SlugField(default='IA9L6LD1BZKH5HRV8W938R9E', max_length=24),
        ),
    ]
