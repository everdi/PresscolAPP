# Generated by Django 2.2.1 on 2019-05-23 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0016_auto_20190523_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos',
            name='slug',
            field=models.SlugField(default='JQAXQ22ILN64GTD7E7JSDTB7', max_length=24),
        ),
    ]
