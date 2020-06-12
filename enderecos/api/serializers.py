from rest_framework import serializers
from enderecos.models import Endereco, Cidade, Estado


class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ['nome']


class CidadeSerializer(serializers.ModelSerializer):
    estado = serializers.StringRelatedField()

    class Meta:
        model = Cidade
        fields = ['nome', 'estado']


class EnderecoSerializer(serializers.ModelSerializer):
    cidade = CidadeSerializer()

    class Meta:
        model = Endereco
        fields = ['id', 'endereco', 'numero', 'bairro', 'latitude', 'longitude', 'cidade']
