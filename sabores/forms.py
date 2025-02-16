from django import forms
from .models import Sabor

class SaborForm(forms.ModelForm):
    class Meta:
        model = Sabor
        fields = ['nombre', 'descripcion']
