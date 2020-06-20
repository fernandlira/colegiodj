from django import forms
from .models import Alumno, Profesor, Curso, Asistencia

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['identifier', 'name', 'last_name']

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['identifier', 'name', 'lastname']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['name']

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ['identifier_profesor', 'identifier_alumno', 'curso', 'fecha', 'asistencia', 'nota']
