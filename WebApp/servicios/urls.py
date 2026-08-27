from django.urls import path
from .views import ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView, ClienteInactivoListView, ClienteRestoreView

urlpatterns = [
    path('clientes/', ClienteListView.as_view(), name='lista_clientes'),
    path('clientes/nuevo', ClienteCreateView.as_view(), name='crear_cliente'),
    path('clientes/<pk>/update', ClienteUpdateView.as_view(), name='actualizar_cliente'),
    path('clientes/<pk>/delete', ClienteDeleteView.as_view(), name='eliminar_cliente'),
    path('clientes/inactivos', ClienteInactivoListView.as_view(), name='clientes_inactivos'),
    path('clientes/<pk>/restore', ClienteRestoreView.as_view(), name='restaurar_cliente'),
]