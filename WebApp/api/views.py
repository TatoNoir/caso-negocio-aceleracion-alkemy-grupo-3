from rest_framework import generics
from servicios.models import Cliente, Servicio, ReservaServicio
from .serializers import (ServicioSerializer, ClienteSerializer,
                          ReservaServicioCalendarSerializer)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


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


class ReservaCalendarAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # FullCalendar envía automáticamente query params ?start=...&end=...
        start_str = request.query_params.get('start')
        end_str = request.query_params.get('end')

        queryset = ReservaServicio.objects.select_related(
            'cliente', 'servicio', 'empleado', 'coordinador'
        )

        if start_str and end_str:
            queryset = queryset.filter(fecha_servicio__range=[start_str, end_str])

        serializer = ReservaServicioCalendarSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)