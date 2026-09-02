from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Servicio, Coordinador, Empleado
from django.views.generic import (ListView, CreateView, UpdateView, View,
                                  DeleteView)
from .forms import ClienteForm, ServicioForm, CoordinadorForm, EmpleadoForm
from django.contrib import messages
from django.urls import reverse_lazy

def lista_clientes(request):
    clientes = Cliente.objects.filter(activo=True)

    return render(request, 'clientes.html', {
        'clientes': clientes
    })

class ClienteListView(ListView):
    model = Cliente
    template_name = 'clientes.html'
    context_object_name = 'clientes'

    def get_queryset(self):
        return Cliente.objects.filter(activo=True)

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'add_cliente.html'

    def get_success_url(self):
        return reverse_lazy('lista_clientes')

class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'update_cliente.html'
    fields = [ 'nombre', 'apellido' ]

    def get_success_url(self):
        return reverse_lazy('lista_clientes')

class ClienteDeleteView(View):

    def post(self, request, pk):
        cliente = Cliente.objects.get(pk=pk)
        cliente.activo = False
        cliente.save()

        return redirect('lista_clientes')

class ClienteInactivoListView(ListView):
    model = Cliente
    template_name = 'clientes_inactivos.html'
    context_object_name = 'clientes'

    def get_queryset(self):
        return Cliente.objects.filter(activo=False)

class ClienteRestoreView(View):
    def post(self, request, pk):
        cliente = Cliente.objects.get(pk=pk)
        cliente.activo = True
        cliente.save()

        messages.success(request, 'Cliente restaurado correctamente.')
        return redirect('clientes_inactivos')

class ServiciosActivosListView(ListView):
    model = Servicio
    context_object_name = "servicios"
    template_name = "servicio_list_activos.html"

    def get_queryset(self):
        return Servicio.objects.filter(activo=True)


class ServicioCreateView(CreateView):
    model = Servicio
    template_name = "servicio_create.html"
    form_class = ServicioForm
    success_url = reverse_lazy("listar_servicios")


class ServicioDetalleUpdateView(UpdateView):
    model = Servicio
    form_class = ServicioForm
    template_name = "servicio_detalle.html"
    context_object_name = "servicio"
    success_url = reverse_lazy("listar_servicios")


class ServicioDeleteView(View):
    def post(self, request, pk):
        servicio = get_object_or_404(Servicio, pk=pk)
        servicio.activo = False
        servicio.save()

        return redirect("listar_servicios")


class ServicioInactivosListView(ListView):
    model = Servicio
    template_name = "servicio_list_inactivos.html"
    context_object_name = "servicios"

    def get_queryset(self):
        return Servicio.objects.filter(activo=False)


def restaurar_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    servicio.activo = True
    servicio.save()
    return redirect("listar_servicios")


class CoordinadoresActivosView(ListView):
    model = Coordinador
    context_object_name = "coordinadores"
    template_name = "coordinador/coordinadores_list_activos.html"

    def get_queryset(self):
        return Coordinador.objects.filter(activo=True)

class CoordinadoresInactivosView(ListView):
    model = Coordinador
    context_object_name = "coordinadores"
    template_name = "coordinador/coordinadores_list_inactivos.html"

    def get_queryset(self):
        return Coordinador.objects.filter(activo=False)

class CoordinadorCreateView(CreateView):
    model = Coordinador
    form_class = CoordinadorForm
    template_name = 'coordinador/coordinador_create.html'

    def get_success_url(self):
        return reverse_lazy('lista_coordinadores')

class CoordinadorUpdateView(UpdateView):
    model = Coordinador
    template_name = 'coordinador/coordinador_update.html'
    form_class = CoordinadorForm

    def get_success_url(self):
        return reverse_lazy('lista_coordinadores')


class CoordinadorDeleteView(View):
    def post(self, request, pk):
        coordinador = get_object_or_404(Coordinador, pk=pk)
        coordinador.activo = False
        coordinador.save()

        return redirect("lista_coordinadores")


def restaurar_coordinador(request, pk):
    coordinador = get_object_or_404(Coordinador, pk=pk)
    coordinador.activo = True
    coordinador.save()

    return redirect('coordinadores_inactivos')




class EmpleadosActivosView(ListView):
    model = Empleado
    context_object_name = "empleados"
    template_name = "empleado/empleados_list_activos.html"

    def get_queryset(self):
        return Empleado.objects.filter(activo=True)

class EmpleadosInactivosView(ListView):
    model = Empleado
    context_object_name = "empleados"
    template_name = "empleado/empleados_list_inactivos.html"

    def get_queryset(self):
        return Empleado.objects.filter(activo=False)


class EmpleadoCreateView(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado/empleado_create.html'

    def get_success_url(self):
        return reverse_lazy('lista_empleados')

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = 'empleado/empleado_update.html'
    form_class = EmpleadoForm

    def get_success_url(self):
        return reverse_lazy('lista_empleados')

class EmpleadoDeleteView(View):
    def post(self, request, pk):
        empleado = get_object_or_404(Empleado, pk=pk)
        empleado.activo = False
        empleado.save()

        return redirect("lista_empleados")

def restaurar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    empleado.activo = True
    empleado.save()

    return redirect('empleados_inactivos')