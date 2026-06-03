from django import forms
from .models import Receta, Comentario

class Formulario_receta(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['titulo', 'ingredientes', 'pasos_elaboracion', 'tiempo_preparacion', 'categoria', 'imagen']

class Formulario_comentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']