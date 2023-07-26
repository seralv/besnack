from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .models import Cliente, Empleado, Plato, Pedido, DetallePedido
from .serializers import ClienteSerializer, EmpleadoSerializer, PlatoSerializer, PedidoSerializer, DetallePedidoSerializer, UserSerializer

class ClienteListCreateView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class EmpleadoListCreateView(generics.ListCreateAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    permission_classes = [AllowAny]

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class PlatoListCreateView(generics.ListCreateAPIView):
    queryset = Plato.objects.all()
    serializer_class = PlatoSerializer

class PedidoListCreateView(generics.ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class PedidoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
