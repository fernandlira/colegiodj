from django import forms
from .models import Alumno, Curso, Asistencia, Nota, Comentario


class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ["name", "last_name"]


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ["name"]


class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ["profesor", "alumno", "fecha", "asistencia"]


class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ["asistencia", "curso", "tipo", "nota"]

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ["asistencia", "comentario"]

