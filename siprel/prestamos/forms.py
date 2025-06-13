from django import forms
from .models import Solicitud

class SolicitudPublicaForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['nombre', 'correo', 'descripcion']
