from django.db.models import Avg
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
    template_name = 'nuevos/cliente_listado.html'
    context_object_name = 'clientes'
    paginate_by = 8

    def get_queryset(self):
        return Cliente.objects.filter(activo=True)

    def get_context_data(self, *, object_list = ..., **kwargs):
        context = super().get_context_data(**kwargs)
        context["enlace"] = "crear_cliente"
        context["descripcion_btn_primario"] = "Crear nuevo cliente"
        context["pre_titulo"] = "Clientes"
        context["titulo"] = "Activos"
        context["activo_clientes"] = "active"
        return context


class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'nuevos/cliente_creacion.html'

    def get_success_url(self):
        return reverse_lazy('lista_clientes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pre_titulo"] = "Clientes"
        context["titulo"] = "Crear nuevo cliente"
        context["activo_clientes"] = "active"
        return context


class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'nuevos/cliente_detalle.html'
    form_class = ClienteForm

    def get_success_url(self):
        return reverse_lazy('lista_clientes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pre_titulo"] = "Clientes"
        context["titulo"] = "Actualizar"
        context["activo_clientes"] = "active"
        return context


class ClienteDeleteView(View):

    def post(self, request, pk):
        cliente = Cliente.objects.get(pk=pk)
        cliente.activo = False
        cliente.save()

        return redirect('lista_clientes')

class ClienteInactivoListView(ListView):
    model = Cliente
    template_name = 'nuevos/cliente_listado.html'
    context_object_name = 'clientes'
    paginate_by = 8

    def get_queryset(self):
        return Cliente.objects.filter(activo=False)

    def get_context_data(self, *, object_list = ..., **kwargs):
        context = super().get_context_data(**kwargs)
        context["enlace"] = "crear_cliente"
        context["pre_titulo"] = "Clientes"
        context["titulo"] = "Inactivos"
        context["descripcion_btn_primario"] = "Crear nuevo cliente"
        context["activo_clientes"] = "active"
        return context

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
    template_name = "nuevos/servicio_listado.html"
    paginate_by = 8

    def get_queryset(self):
        return Servicio.objects.filter(activo=True)

    def get_context_data(self, *, object_list = ..., **kwargs):
        context = super().get_context_data(**kwargs)
        context["enlace"] = "crear_servicio"
        context["descripcion_btn_primario"] = "Crear nuevo servicio"
        context["pre_titulo"] = "Servicios"
        context["titulo"] = "Activos"
        context["activo_servicios"] = "active"
        return context


class ServicioCreateView(CreateView):
    model = Servicio
    template_name = "nuevos/servicio_creacion.html"
    form_class = ServicioForm
    success_url = reverse_lazy("listar_servicios")

    def get_context_data(self, *, object_list = ..., **kwargs):
        context = super().get_context_data(**kwargs)
        context["pre_titulo"] = "Servicios"
        context["titulo"] = "Crear nuevo servicio"
        context["activo_servicios"] = "active"
        return context


class ServicioDetalleUpdateView(UpdateView):
    model = Servicio
    form_class = ServicioForm
    template_name = "nuevos/servicio_detalle.html"
    context_object_name = "servicio"
    success_url = reverse_lazy("listar_servicios")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pre_titulo"] = "Servicios"
        context["titulo"] = "Actualizar servicio"
        context["activo_servicios"] = "active"
        return context


class ServicioDeleteView(View):
    def post(self, request, pk):
        servicio = get_object_or_404(Servicio, pk=pk)
        servicio.activo = False
        servicio.save()

        return redirect("listar_servicios")


class ServicioInactivosListView(ListView):
    model = Servicio
    template_name = "nuevos/servicio_listado.html"
    context_object_name = "servicios"
    paginate_by = 8

    def get_queryset(self):
        return Servicio.objects.filter(activo=False)

    def get_context_data(self, *, object_list = ..., **kwargs):
        context = super().get_context_data(**kwargs)
        context["enlace"] = "crear_servicio"
        context["descripcion_btn_primario"] = "Crear nuevo servicio"
        context["pre_titulo"] = "Servicios"
        context["titulo"] = "Inactivos"
        context["activo_servicios"] = "active"
        return context


def restaurar_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    servicio.activo = True
    servicio.save()
    return redirect("listar_servicios_inactivos")


class CoordinadoresActivosView(ListView):
    model = Coordinador
    context_object_name = "coordinadores"
    template_name = "nuevos/coordinador_listado.html"
    paginate_by = 8

    def get_queryset(self):
        return Coordinador.objects.filter(activo=True)

    def get_context_data(self, *, object_list = ..., **kwargs):
        context = super().get_context_data(**kwargs)
        context["enlace"] = "crear_coordinador"
        context["descripcion_btn_primario"] = "Crear nuevo coordinador"
        context["pre_titulo"] = "Coordinadores"
        context["titulo"] = "Activos"
        context["activo_coordinadores"] = "active"
        return context


class CoordinadoresInactivosView(ListView):
    model = Coordinador
    context_object_name = "coordinadores"
    template_name = "nuevos/coordinador_listado.html"
    paginate_by = 8

    def get_queryset(self):
        return Coordinador.objects.filter(activo=False)

    def get_context_data(self, *, object_list = ..., **kwargs):
        context = super().get_context_data(**kwargs)
        context["enlace"] = "crear_coordinador"
        context["descripcion_btn_primario"] = "Crear nuevo coordinador"
        context["pre_titulo"] = "Coordinadores"
        context["titulo"] = "Inactivos"
        context["activo_coordinadores"] = "active"
        return context


class CoordinadorCreateView(CreateView):
    model = Coordinador
    form_class = CoordinadorForm
    template_name = 'nuevos/coordinador_creacion.html'

    def get_success_url(self):
        return reverse_lazy('lista_coordinadores')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pre_titulo"] = "Coordinadores"
        context["titulo"] = "Crear nuevo coordinador"
        return context


class CoordinadorUpdateView(UpdateView):
    model = Coordinador
    template_name = 'nuevos/coordinador_detalle.html'
    form_class = CoordinadorForm

    def get_success_url(self):
        return reverse_lazy('lista_coordinadores')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pre_titulo"] = "Coordinadores"
        context["titulo"] = "Actualizar"
        return context


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
    template_name = "nuevos/empleado_listado.html"
    paginate_by = 8

    def get_queryset(self):
        return Empleado.objects.filter(activo=True)

    def get_context_data(self, *, object_list = ..., **kwargs):
        context = super().get_context_data(**kwargs)
        context["enlace"] = "crear_empleado"
        context["descripcion_btn_primario"] = "Crear nuevo empleado"
        context["pre_titulo"] = "Empleados"
        context["titulo"] = "Activos"
        context["activo_empleados"] = "active"
        return context


class EmpleadosInactivosView(ListView):
    model = Empleado
    context_object_name = "empleados"
    template_name = "nuevos/empleado_listado.html"
    paginate_by = 8

    def get_queryset(self):
        return Empleado.objects.filter(activo=False)

    def get_context_data(self, *, object_list = ..., **kwargs):
        context = super().get_context_data(**kwargs)
        context["enlace"] = "crear_empleado"
        context["descripcion_btn_primario"] = "Crear nuevo empleado"
        context["pre_titulo"] = "Empleados"
        context["titulo"] = "Inactivos"
        context["activo_empleados"] = "active"
        return context


class EmpleadoCreateView(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'nuevos/empleado_creacion.html'

    def get_success_url(self):
        return reverse_lazy('lista_empleados')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pre_titulo"] = "Empleados"
        context["titulo"] = "Crear nuevo empleado"
        context["activo_empleados"] = "active"
        return context


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = 'nuevos/empleado_detalle.html'
    form_class = EmpleadoForm

    def get_success_url(self):
        return reverse_lazy('lista_empleados')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pre_titulo"] = "Empleados"
        context["titulo"] = "Actualizar"
        context["activo_empleados"] = "active"
        return context


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
        "empleados_activos": Empleado.objects.filter(activo=True).count(),
        "coordinadores_activos": Coordinador.objects.filter(activo=True).count(),

        "enlace" : "inicio",
        "descripcion_btn_primario": "Crear una reserva | Lleva a inicio para no romper",
        "pre_titulo": "Resumen",
        "titulo": "Tablero",
        "descripcion_btn_secundario": "Nuevo servicio",
        "activo_inicio": "active"
    }
    return render(request, "nuevos/main.html", context)