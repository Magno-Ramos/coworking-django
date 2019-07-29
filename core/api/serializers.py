from rest_framework import serializers

from core.models import Coworking
from enderecos.api.serializers import EnderecoSerializer


class CoworkingSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()

    class Meta:
        model = Coworking
        fields = ['id', 'logo', 'nome', 'descricao', 'ativo', 'status', 'endereco']
