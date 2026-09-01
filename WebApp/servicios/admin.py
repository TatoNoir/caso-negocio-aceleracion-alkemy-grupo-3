from django.contrib import admin

from .models import Coordinador, Empleado, Servicio, Cliente
# Register your models here.

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion", "precio", "activo")
    search_fields = ("nombre",)
    list_filter = ("activo",)

    def delete_model(self, request, obj):
        ''' Cambia la eliminacion fisica por una eliminacion logica '''
        obj.activo = False
        obj.save()

    def delete_queryset(self, request, queryset):
        ''' Este metodo me permite sobreescribir el comportamiento de
         la eliminacion multiple que hay en la interfaz Admin '''
        queryset.update(activo=False)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "activo")
    list_filter = ("activo",)
    search_fields = ("nombre", "apellido")

    def delete_model(self, request, obj):
        ''' Cambia la eliminacion fisica por una eliminacion logica '''
        obj.activo = False
        obj.save()

    def delete_queryset(self, request, queryset):
        ''' Este metodo me permite sobreescribir el comportamiento de
         la eliminacion multiple que hay en la interfaz Admin '''
        queryset.update(activo=False)

@admin.register(Coordinador)
class CoordinadorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "numero_documento", "fecha_alta", "activo")
    list_filter = ("activo",)
    search_fields = ("nombre", "apellido")

    def delete_model(self, request, obj):
        ''' Cambia la eliminacion fisica por una eliminacion logica '''
        obj.activo = False
        obj.save()

    def delete_queryset(self, request, queryset):
        ''' Este metodo me permite sobreescribir el comportamiento de
         la eliminacion multiple que hay en la interfaz Admin '''
        queryset.update(activo=False)


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "numero_legajo", "activo")
    list_filter = ("activo",)
    search_fields = ("nombre", "apellido")

    def delete_model(self, request, obj):
        ''' Cambia la eliminacion fisica por una eliminacion logica '''
        obj.activo = False
        obj.save()

    def delete_queryset(self, request, queryset):
        ''' Este metodo me permite sobreescribir el comportamiento de
         la eliminacion multiple que hay en la interfaz Admin '''
        queryset.update(activo=False)