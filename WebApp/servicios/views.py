import calendar
from datetime import datetime, date
from django.db.models import Avg, Count
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, ReservaServicio, Servicio, Coordinador, Empleado
from django.views.generic import (ListView, CreateView, UpdateView, View,
                                  DeleteView)
from .forms import ClienteForm, ReservaServicioForm, ServicioForm, CoordinadorForm, EmpleadoForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils import timezone

def lista_clientes(request):
    clientes = Cliente.objects.filter(activo=True)

    return render(request, 'clientes.html', {
        'clientes': clientes
    })

class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente/cliente_listado.html'
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
    template_name = 'cliente/cliente_creacion.html'

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
    template_name = 'cliente/cliente_detalle.html'
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
    template_name = 'cliente/cliente_listado.html'
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
    template_name = "servicio/servicio_listado.html"
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
    form_class = ServicioForm
    template_name = "servicio/servicio_creacion.html"
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
    template_name = "servicio/servicio_detalle.html"
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
    template_name = "servicio/servicio_listado.html"
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
    template_name = "coordinador/coordinador_listado.html"
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
    template_name = "coordinador/coordinador_listado.html"
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
    template_name = 'coordinador/coordinador_creacion.html'

    def get_success_url(self):
        return reverse_lazy('lista_coordinadores')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pre_titulo"] = "Coordinadores"
        context["titulo"] = "Crear nuevo coordinador"
        return context


class CoordinadorUpdateView(UpdateView):
    model = Coordinador
    template_name = 'coordinador/coordinador_detalle.html'
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
    template_name = "empleado/empleado_listado.html"
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
    template_name = "empleado/empleado_listado.html"
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
    template_name = 'empleado/empleado_creacion.html'

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
    template_name = 'empleado/empleado_detalle.html'
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

        "enlace" : "crear_reserva",
        "descripcion_btn_primario": "Crear una reserva",
        "pre_titulo": "Resumen",
        "titulo": "Tablero",
        "descripcion_btn_secundario": "Nuevo servicio",
        "activo_inicio": "active",

        "cliente_mas_recurrente": Cliente.objects.annotate(total_reservas=
                                                           Count("reservas"))
        .order_by("-total_reservas").first(),

    }

    return render(request, "main.html", context)


class ReservasView(ListView):
    model = ReservaServicio
    context_object_name = "reservas"
    template_name = "reserva/reserva_listado.html"
    paginate_by = 8

    def get_context_data(self, *, object_list = ..., **kwargs):
        context = super().get_context_data(**kwargs)
        context["enlace"] = "crear_reserva"
        context["descripcion_btn_primario"] = "Crear nueva reserva"
        context["pre_titulo"] = "Reservas"
        context["titulo"] = "Listado"
        context["activo_reservas"] = "active"
        context["now"] = timezone.now()
        return context


class ReservaCreateView(CreateView):
    model = ReservaServicio
    form_class = ReservaServicioForm
    template_name = 'reserva/reserva_creacion.html'
    success_url = reverse_lazy('lista_reservas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pre_titulo"] = "Reservas"
        context["titulo"] = "Crear nueva reserva"
        context["activo_reservas"] = "active"
        return context

    def get_initial(self):
        initial = super().get_initial()
        servicio_id = self.request.GET.get('servicio')

        if servicio_id:
            servicio = get_object_or_404(Servicio, pk=servicio_id, activo=True)
            initial['servicio'] = servicio

        return initial


class ReservaUpdateView(UpdateView):
    model = ReservaServicio
    template_name = 'reserva/reserva_detalle.html'
    form_class = ReservaServicioForm
    success_url = reverse_lazy('lista_reservas')
    context_object_name = "reserva"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pre_titulo"] = "Reservas"
        context["titulo"] = "Actualizar"
        context["activo_reservas"] = "active"
        return context

class ReservaDeleteView(DeleteView):
    model = ReservaServicio
    success_url = reverse_lazy('lista_reservas')


THEMES = ("light", "dark")
def capturar_tema(request):
    ''' Permite cambiar el tema del sitio'''
    theme = request.GET.get("theme", "light")

    if theme not in THEMES:
        theme = "light"
    return {"theme": theme}