from django.db import models
from core.models import Coworking


# Create your models here.
class Sala(models.Model):
    nome = models.CharField(max_length=150)
    numero = models.IntegerField()
    descricao = models.TextField(blank=True, null=True)
    coworking = models.ForeignKey(Coworking, on_delete=models.CASCADE)

    def __str__(self):
        if self.nome:
            return self.nome
        else:
            return self.numero


class FotosSala(models.Model):
    image = models.ImageField(upload_to='imagens/salas')
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name='fotos')

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos de Salas'
