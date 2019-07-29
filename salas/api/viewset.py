from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from salas.models import Sala
from .serializers import SalaSerializer


class SalaViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]

    queryset = Sala.objects.all()
    serializer_class = SalaSerializer
    filterset_fields = ['coworking']
