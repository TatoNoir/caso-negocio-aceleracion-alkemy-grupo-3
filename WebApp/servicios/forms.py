from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Cliente, ReservaServicio, Servicio, Empleado, Coordinador

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
        fields = ['nombre', 'apellido', 'numero_documento']

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
        }

class ReservaServicioForm(forms.ModelForm):
    class Meta:
        model = ReservaServicio
        fields = ['cliente', 'servicio', 'empleado', 'coordinador', 'fecha_servicio']

        widgets = {
            'cliente': forms.Select(attrs={
                'class': 'form-control',
            }),
            'servicio': forms.Select(attrs={
                'class': 'form-control',
            }),
            'empleado': forms.Select(attrs={
                'class': 'form-control',
            }),
            'coordinador': forms.Select(attrs={
                'class': 'form-control',
            }),
            'fecha_servicio': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['cliente'].queryset = Cliente.objects.filter(activo=True)
        self.fields['servicio'].queryset = Servicio.objects.filter(activo=True)
        self.fields['empleado'].queryset = Empleado.objects.filter(activo=True)
        self.fields['coordinador'].queryset = Coordinador.objects.filter(activo=True)

    def clean_fecha_servicio(self):
        fecha = self.cleaned_data['fecha_servicio']

        if fecha < timezone.now():
            raise ValidationError(
                'La fecha del servicio no puede ser anterior a hoy.'
            )

        return fecha