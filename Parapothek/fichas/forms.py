from django import forms
from django.forms import CheckboxSelectMultiple, TextInput
from django.core.exceptions import ValidationError

from .models import Inventario,Puntuar,Indicacion


        

class PuntuarForm(forms.ModelForm):
    class Meta:
        model = Puntuar
        fields = '__all__'
        
class InventarioIndicacionesForm(forms.ModelForm):
        
        class Meta:
            model = Inventario
            fields = ('indicaciones',)
            widgets = {
            'indicaciones': CheckboxSelectMultiple,}

class IndicacionesForm(forms.ModelForm):
     
    class Meta:
        model = Indicacion
        fields = ('__all__')
        widgets = {
            'nombre':forms.TextInput,
            'zona': forms.CheckboxSelectMultiple,
        }            