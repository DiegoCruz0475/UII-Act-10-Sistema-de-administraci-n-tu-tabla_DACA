from django import forms 
from .models import Cliente 

class ClienteForm(forms.ModelForm):
    class Meta: 
        model = Cliente 
        fields = ['nombre', 'apellido', 'correo', 'telefono', 'direccion', 'fecha_nacimiento']
        labels = {
            'nombre':'Nombre',
            'apellido':'Apellido',
            'correo':'Correo',
            'telefono':'Telefono',
            'direccion':'Direccion',
            'fecha_nacimiento':'Nacimiento',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control'}),

        }