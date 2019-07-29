from rest_framework.viewsets import ModelViewSet
from usuarios.api.serializers import UsuarioSerializer
from usuarios.models import Usuario


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer