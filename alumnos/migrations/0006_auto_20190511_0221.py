# Generated by Django 2.0.5 on 2019-05-11 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0005_auto_20190511_0208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos',
            name='slug',
            field=models.SlugField(default='GCY3YI4YXHPAUMHPQY2SB5PA', max_length=24),
        ),
    ]