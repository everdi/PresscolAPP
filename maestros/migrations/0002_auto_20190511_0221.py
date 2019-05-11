# Generated by Django 2.0.5 on 2019-05-11 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('padres', '0001_initial'),
        ('alumnos', '0006_auto_20190511_0221'),
        ('maestros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiarioTrabajo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DT_fecha', models.DateField(auto_now_add=True)),
                ('DT_descripcion', models.TextField()),
                ('DT_actividadApoyo', models.TextField()),
                ('DT_necesidades', models.TextField()),
                ('DT_alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.alumnos')),
                ('DT_maestro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='padres.Profesor')),
            ],
        ),
        migrations.CreateModel(
            name='grupos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gru_clave', models.CharField(max_length=10)),
                ('gru_salon', models.CharField(default='', max_length=10)),
                ('gru_grado', models.IntegerField(null=True)),
                ('gru_alumnos', models.ManyToManyField(to='alumnos.alumnos')),
                ('gru_maestro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Maestro', to='padres.Profesor')),
            ],
        ),
        migrations.RemoveField(
            model_name='maestro',
            name='pro_nombre',
        ),
        migrations.DeleteModel(
            name='Maestro',
        ),
    ]