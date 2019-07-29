from rest_framework.viewsets import ModelViewSet
from .serializers import AgendamentoSerializer
from agendamentos.models import Agendamento


class AgendamentoViewSet(ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
