from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .serializers import AgendamentoSerializer
from agendamentos.models import Agendamento


class AgendamentoViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
