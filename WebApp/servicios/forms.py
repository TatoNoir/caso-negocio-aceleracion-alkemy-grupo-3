from django import forms
from .models import Cliente, Servicio, Empleado, Coordinador

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido']

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre',
            }),
            'apellido': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el apellido',
            }),
        }


class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion', "precio"]

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre',
            }),
            'descripcion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese una descripcion',
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el precio',
            }),
        }

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido', 'numero_legajo']

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre',
            }),
            'apellido': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el apellido',
            }),
            'numero_legajo': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el numero de legajo'
            }),
        }

class CoordinadorForm(forms.ModelForm):
    class Meta:
        model = Coordinador
        fields = ['nombre', 'apellido', 'numero_documento', 'fecha_alta']

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre',
            }),
            'apellido': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el apellido',
            }),
            'numero_documento': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el numero de documento'
            }),
            'fecha_alta': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            })
        }