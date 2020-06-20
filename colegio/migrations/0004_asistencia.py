# Generated by Django 3.0.7 on 2020-06-20 18:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0003_curso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('asistencia', models.CharField(choices=[('Asistio', 'Asistio'), ('No-asistio', 'No asistio')], max_length=100)),
                ('nota', models.IntegerField(blank=True, null=True)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colegio.Alumno')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colegio.Curso')),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colegio.Profesor')),
            ],
            options={
                'verbose_name': 'Asistencia del alumno',
                'verbose_name_plural': 'Asistencia de los alumnos',
                'ordering': ['alumno'],
            },
        ),
    ]
