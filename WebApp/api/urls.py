from django.urls import path
from .views import (ServicioListView, ServicioDetalleView,
                    ClienteListView, ClienteDetalleView, ReservaCalendarAPIView)
from drf_spectacular.views import (SpectacularAPIView, SpectacularSwaggerView)


urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path('servicios/', ServicioListView.as_view(), name='api_lista_servicios'),
    path('servicios/<int:servicio_id>/', ServicioDetalleView.as_view(), name='api_detalle_servicio'),
    path('clientes/', ClienteListView.as_view(), name='api_lista_clientes'),
    path('clientes/<int:cliente_id>/', ClienteDetalleView.as_view(), name='api_detalle_cliente'),

    path('api/reservas-calendar/', ReservaCalendarAPIView.as_view(), name='api_reservas_calendar'),
]
