from rest_framework import serializers
from servicios.models import Cliente, Servicio, ReservaServicio
from django.utils import timezone


class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ['id', 'nombre', 'descripcion', 'precio', 'activo']


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'apellido', 'activo']


class ReservaServicioCalendarSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    start = serializers.SerializerMethodField()
    extendedProps = serializers.SerializerMethodField()

    class Meta:
        model = ReservaServicio
        fields = ['id', 'title', 'start', 'extendedProps']

    def get_title(self, obj):
        return f"{obj.servicio}"

    def get_start(self, obj):
        fecha_local = timezone.localtime(obj.fecha_servicio)
        return fecha_local.isoformat()

    def get_extendedProps(self, obj):
        return {
            'cliente': str(obj.cliente),
            'servicio': str(obj.servicio),
            'empleado': str(obj.empleado),
            'coordinador': str(obj.coordinador),
        }