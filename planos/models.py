from django.db import models
from salas.models import Sala


# Create your models here.
class Plano(models.Model):
    PERIDO_CHOICES = [
        ('HORA', '1 Hora'),
        ('4_HORAS', '4 Horas'),
        ('DIA_8H', '1 Diária (8 Horas)'),
        ('DIA_12H', '1 Diária (12 Horas)'),
        ('DIA_24H', '1 Diária (24 Horas)'),
        ('SEMANA', '1 Semana'),
        ('QUINZENA', '1 Quinzena'),
        ('MES', '1 Mês'),
        ('TRIMESTRE', 'Trimestre - 3 Meses'),
        ('SEMESTRE', 'Semestre - 6 Meses'),
        ('SEMESTRE', '1 Ano'),
    ]

    nome = models.CharField(max_length=150)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    periodo = models.CharField(max_length=150, choices=PERIDO_CHOICES)
    sala = models.ForeignKey(Sala, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome
