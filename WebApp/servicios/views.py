from django.db.models import Avg
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Servicio
from django.views.generic import (ListView, CreateView, UpdateView, View,
                                  DeleteView)
from .forms import ClienteForm, ServicioForm
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


def metricas_home(request):
    context = {
        "clientes_activos": Cliente.objects.filter(activo=True).count(),
        "servicios_activos": Servicio.objects.filter(activo=True).count(),
        "servicio_mas_barato": Servicio.objects.filter(activo=True) \
            .order_by("precio").first(),
        "servicio_mas_caro" : Servicio.objects.filter(activo=True) \
            .order_by("-precio").first(),
        "precio_promedio" : Servicio.objects.filter(activo=True).aggregate(
            promedio=Avg("precio"))["promedio"],
    }
    return render(request, "nuevos/main.html", context)