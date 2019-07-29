from django.db import models
from usuarios.models import Usuario


# Create your models here.
class Cliente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.PROTECT)
    CPF = models.CharField(max_length=45)

    def __str__(self):
        return self.usuario.user.username
