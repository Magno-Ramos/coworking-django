from django.db import models
from salas.models import Sala


# Create your models here.
from usuarios.models import Usuario


class Status(models.Model):
    STATUS_CHOICE = [
        ('SOLICITADO', 'Solicitado'),
        ('AGUARDANDO_PAGAMENTO', 'Aguardando Pagamento'),
        ('CONFIRMADO', 'Confirmado'),
        ('SOLICITAR_CANCELAMENTO', 'Cancelamento Solicitado'),
        ('CANCELADO', 'Cancelado'),
    ]

    status = models.CharField(max_length=150, choices=STATUS_CHOICE)
    mensagem = models.TextField()


class Agendamento(models.Model):

    STATUS_CHOICE = [
        ('SOLICITADO', 'Solicitado'),
        ('AGUARDANDO_PAGAMENTO', 'Aguardando Pagamento'),
        ('CONFIRMADO', 'Confirmado'),
        ('SOLICITAR_CANCELAMENTO', 'Cancelamento Solicitado'),
        ('CANCELADO', 'Cancelado'),
    ]

    solicitante = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    horario_inicio = models.DateTimeField()
    horario_termino = models.DateTimeField()
    status = models.OneToOneField(Status, on_delete=models.PROTECT)
    salas = models.ManyToManyField(Sala)

    def __str__(self):
        return '{} - {}'.format(self.horario_inicio, self.horario_termino)
