from django.urls import path
from .views import ClienteListCreateView, EmpleadoListCreateView, PlatoListCreateView, PedidoListCreateView, PedidoDetailView, UserCreateView

urlpatterns = [
    path('clientes/', ClienteListCreateView.as_view(), name='cliente-list-create'),
    path('empleados/', EmpleadoListCreateView.as_view(), name='empleado-list-create'),
    path('register/', UserCreateView.as_view(), name='user-create'),
    path('platos/', PlatoListCreateView.as_view(), name='plato-list-create'),
    path('pedidos/', PedidoListCreateView.as_view(), name='pedido-list-create'),
    path('pedidos/<int:pk>/', PedidoDetailView.as_view(), name='pedido-detail'),
]
