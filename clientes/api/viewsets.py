from rest_framework.viewsets import ModelViewSet
from clientes.models import Cliente
from clientes.api.serializers import ClienteSerializer


class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
