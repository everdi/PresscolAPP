# Generated by Django 2.2.1 on 2019-05-09 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos',
            name='slug',
            field=models.SlugField(default='8GZC68JYZR74DOGC2EO0QZQD', max_length=24),
        ),
    ]