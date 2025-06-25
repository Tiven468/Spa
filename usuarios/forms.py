from django import forms
from .models import Agregarservicio

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Agregarservicio
        fields = ['nombre', 'descripcion', 'precio', 'imagen']