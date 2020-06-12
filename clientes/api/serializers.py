from rest_framework.serializers import ModelSerializer
from usuarios.api.serializers import UsuarioSerializer
from clientes.models import Cliente


class ClienteSerializer(ModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = Cliente
        fields = ['id', 'usuario', 'CPF']
