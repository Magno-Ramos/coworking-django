from django.db import models


# Create your models here.
class Estado(models.Model):
    nome = models.CharField(max_length=150)
    sigla = models.CharField(max_length=5)

    def __str__(self):
        return self.nome


class Cidade(models.Model):
    nome = models.CharField(max_length=150)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Endereco(models.Model):
    endereco = models.CharField(max_length=255)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=150)
    latitude = models.IntegerField(blank=True, null=True)
    longitude = models.IntegerField(blank=True, null=True)
    cidade = models.ForeignKey(Cidade, related_name='cidade', on_delete=models.PROTECT)

    def __str__(self):
        return '{} - {}'.format(self.endereco, self.numero)
