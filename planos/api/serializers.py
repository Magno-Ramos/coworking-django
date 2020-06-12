from rest_framework.serializers import ModelSerializer
from planos.models import Plano


class PlanoSerializer(ModelSerializer):
    class Meta:
        model = Plano
        fields = ['nome', 'preco', 'periodo', 'sala']
