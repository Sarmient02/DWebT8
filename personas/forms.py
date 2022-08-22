from django import forms

from .models import Ciudad, TipoDocumento, Persona

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

class CiudadesForm(forms.ModelForm):

    class Meta:
        model = Ciudad
        
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

class DateInput(forms.DateInput):
    input_type = 'date'
    

class PersonasForm(forms.ModelForm):
    class Meta:
        model = Persona
        
        fields = [
            'name',
            'lastname',
            'tipodocumento',
            'documento',
            'lugarnacimiento',
            'fechanacimiento',
            'email',
            'telefono',
            'username',
            'password'
        ]
        labels = {
            'name':'Nombres',
            'lastname':'Apellidos',
            'tipodocumento':'Tipo de Documento',
            'documento': 'Documento',
            'lugarnacimiento': 'Lugar de Nacimiento',
            'fechanacimiento': 'Fecha de Nacimiento',
            'email': 'Email',
            'telefono': 'Teléfono',
            'username': 'Usuario',
            'password': 'Contraseña'#,
            #'cpassword': 'Confirmar Contraseña'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'input','required':''}),
            'lastname': forms.TextInput(attrs={'class':'input','required':''}),
            'tipodocumento':forms.TextInput(attrs={'class':'input','required':''}),
            'documento': forms.TextInput(attrs={'class':'input','required':''}),
            'lugarnacimiento': forms.TextInput(attrs={'class':'input','required':''}),
            'fechanacimiento': DateInput(attrs={'class':'input', 'required':''}),
            'email': forms.EmailInput(attrs={'class':'input','required':''}),
            'telefono': forms.TextInput(attrs={'class':'input','required':''}),
            'username': forms.TextInput(attrs={'class':'input','required':''}),
            'password': forms.PasswordInput(attrs={'class':'input','required':''})#,
            #'cpassword': forms.PasswordInput(attrs={'class':'input','required':''})
        }
    
    #def clean(self):
     #   cleaned_data = super().clean()
      #  valpwd = self.cleaned_data['password']
       # valcpwd = self.cleaned_data['cpassword']
       # if valpwd != valcpwd:
        #    raise forms.ValidationError('Las contraseñas no coinciden')