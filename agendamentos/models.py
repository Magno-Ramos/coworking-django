from django.db import models
from salas.models import Sala
from django.utils.timezone import now

# Create your models here.
from usuarios.models import Usuario


class Agendamento(models.Model):
    STATUS_CHOICE = [
        ('SOLICITADO', 'Solicitado'),
        ('AGUARDANDO_PAGAMENTO', 'Aguardando Pagamento'),
        ('CONFIRMADO', 'Confirmado'),
        ('SOLICITAR_CANCELAMENTO', 'Cancelamento Solicitado'),
        ('CANCELADO', 'Cancelado'),
    ]

    solicitante = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    horario_inicio = models.DateTimeField(editable=True, blank=False, default=now)
    horario_termino = models.DateTimeField(editable=True, blank=False, default=now)
    status = models.CharField(max_length=45, choices=STATUS_CHOICE)
    salas = models.ManyToManyField(Sala)

    def __str__(self):
        return '{} - {}'.format(self.horario_inicio, self.horario_termino)
