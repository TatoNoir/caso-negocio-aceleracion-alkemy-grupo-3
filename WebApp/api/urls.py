from django.urls import path
from .views import (ServicioListView, ServicioDetalleView,
                    ClienteListView, ClienteDetalleView)

urlpatterns = [
    path('servicios/', ServicioListView.as_view(), name='api_lista_servicios'),
    path('servicios/<int:servicio_id>/', ServicioDetalleView.as_view(), name='api_detalle_servicio'),
    path('clientes/', ClienteListView.as_view(), name='api_lista_clientes'),
    path('clientes/<int:cliente_id>/', ClienteDetalleView.as_view(), name='api_detalle_cliente'),
]
