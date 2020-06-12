from rest_framework.viewsets import ModelViewSet
from .serializers import PlanoSerializer
from planos.models import Plano


class PlanoViewSet(ModelViewSet):
    queryset = Plano.objects.all()
    serializer_class = PlanoSerializer
    filterset_fields = ['sala']
