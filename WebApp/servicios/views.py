from django.shortcuts import render, redirect
from .models import Cliente
from django.views.generic import ListView, CreateView, UpdateView, View
from .forms import ClienteForm
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