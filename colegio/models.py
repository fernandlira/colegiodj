from django.db import models
from django.utils import timezone

"""# Create your models here.
class Profesor(models.Model):
    id = models.AutoField(primary_key=True)
    identifier = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"
        ordering = ["name"]

    def __str__(self):
        return self.name"""


class Alumno(models.Model):
    id = models.AutoField(primary_key=True)
    identifier = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Asistencia(models.Model):
    ASISTENCIA = {
        ("Asistio", "Asistio"),
        ("No-asistio", "No asistio"),
    }
    id = models.AutoField(primary_key=True)
    profesor = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    alumno = models.ForeignKey("Alumno", on_delete=models.CASCADE)
    fecha = models.DateField(null=True, blank=True, default=timezone.now)
    asistencia = models.CharField(
        max_length=100, choices=ASISTENCIA, blank=False, null=False
    )

    class Meta:
        verbose_name = "Asistencia del alumno"
        verbose_name_plural = "Asistencia de los alumnos"
        ordering = ["alumno"]

    def __str__(self):
        return f"Asistencia de {self.alumno} en clase de {self.profesor} en el día {self.fecha}"


class Nota(models.Model):
    TIPO = {
        ("Asistio", "Asistio"),
        ("No-asistio", "No asistio"),
    }
    id = models.AutoField(primary_key=True)
    asistencia = models.ForeignKey("Asistencia", on_delete=models.CASCADE)
    curso = models.ForeignKey("Curso", on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50, choices=TIPO, blank=False, null=False)
    nota = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "Nota"
        verbose_name_plural = "Notas"
        ordering = ["nota"]

    def __str__(self):
        return f"{self.asistencia} - con Nota en {self.curso}"


class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    asistencia = models.ForeignKey("Asistencia", on_delete=models.CASCADE)
    comentario = models.TextField(blank=False, null=False)

    class Meta:
        verbose_name = "Justificación"
        verbose_name_plural = "Justificaciones de las asistencias"

    def __str__(self):
        return f"Comentario sobre asistencia: {self.comentario}"
