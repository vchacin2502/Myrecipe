from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Comentario, Receta

class Formulario_receta(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['titulo', 'ingredientes', 'pasos_elaboracion', 'tiempo_preparacion', 'categoria', 'imagen']

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la receta'}),
            'ingredientes': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Lista de ingredientes separados por líneas o comas'}),
            'pasos_elaboracion': forms.Textarea(attrs={'class': 'form-control', 'rows': 8, 'placeholder': 'Explica el proceso paso a paso'}),
            'tiempo_preparacion': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'placeholder': '45'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class Formulario_comentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']

        widgets = {
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Escribe un comentario útil y concreto'}),
        }


class FormularioRegistro(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
        })