from rest_framework.serializers import ModelSerializer
from agendamentos.models import Agendamento


class AgendamentoSerializer(ModelSerializer):
    class Meta:
        model = Agendamento
        fields = ['id', 'solicitante', 'horario_inicio', 'horario_termino', 'status', 'salas']