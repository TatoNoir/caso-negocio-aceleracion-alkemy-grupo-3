from django.urls import path
from .views import (ClienteListView, ClienteCreateView, ClienteUpdateView,
                    ClienteDeleteView, ClienteInactivoListView,
                    ClienteRestoreView, ServiciosActivosListView,
                    ServicioCreateView, ServicioDetalleUpdateView,
                    ServicioDeleteView, ServicioInactivosListView,
                    restaurar_servicio)

urlpatterns = [
    path('clientes/', ClienteListView.as_view(), name='lista_clientes'),
    path('clientes/nuevo', ClienteCreateView.as_view(), name='crear_cliente'),
    path('clientes/<pk>/update', ClienteUpdateView.as_view(), name='actualizar_cliente'),
    path('clientes/<pk>/delete', ClienteDeleteView.as_view(), name='eliminar_cliente'),
    path('clientes/inactivos', ClienteInactivoListView.as_view(), name='clientes_inactivos'),
    path('clientes/<pk>/restore', ClienteRestoreView.as_view(), name='restaurar_cliente'),
    path("servicios/", ServiciosActivosListView.as_view(),
         name="listar_servicios"),
    path("servicios/nuevo/", ServicioCreateView.as_view(),
         name="crear_servicio"),
    path("servicios/<pk>/detalle/",ServicioDetalleUpdateView.as_view(),
         name="actualizar_servicio"),
    path("servicios/<pk>/delete/", ServicioDeleteView.as_view(),
         name="eliminar_servicio"),
    path("servicios/inactivos", ServicioInactivosListView.as_view(),
         name="listar_servicios_inactivos"),
    path("servicios/<pk>/restaurar/", restaurar_servicio,
         name="restaurar_servicio")
]