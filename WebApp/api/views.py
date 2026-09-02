from rest_framework import generics
from servicios.models import Cliente, Servicio
from .serializers import ServicioSerializer, ClienteSerializer


class ServicioListView(generics.ListAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer


class ServicioDetalleView(generics.RetrieveAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
    lookup_url_kwarg = 'servicio_id'


class ClienteListView(generics.ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ClienteDetalleView(generics.RetrieveAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    lookup_url_kwarg = 'cliente_id'
