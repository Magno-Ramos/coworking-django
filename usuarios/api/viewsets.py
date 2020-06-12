from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from usuarios.api.serializers import UsuarioSerializer
from usuarios.models import Usuario


class UsuarioViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    authentication_classes = [TokenAuthentication]

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
