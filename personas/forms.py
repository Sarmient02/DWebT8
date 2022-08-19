from django import forms

from .models import TipoDocumento

#Formulario para cargar de Documentos

class DocumentosForm(forms.ModelForm):

    class Meta:
        model = TipoDocumento
        
        fields = [
            'nombre',
            'descripcion'
        ]
        labels = {
            'nombre':'Nombre',
            'descripcion':'Descripción'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'input','required':''}),
            'descripcion': forms.TextInput(attrs={'class':'input','required':''})
        }