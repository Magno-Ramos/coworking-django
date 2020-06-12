from rest_framework.serializers import ModelSerializer
from salas.models import Sala, FotosSala


class FotosSalaSerializer(ModelSerializer):
    class Meta:
        model = FotosSala
        fields = ['id', 'image']


class SalaSerializer(ModelSerializer):
    fotos = FotosSalaSerializer(many=True)

    class Meta:
        model = Sala
        fields = ['id', 'nome', 'numero', 'descricao', 'coworking', 'fotos']
