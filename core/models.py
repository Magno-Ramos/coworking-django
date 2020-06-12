from django.db import models
from enderecos.models import Endereco
from clientes.models import Cliente
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    TYPE_CLIENT = 0
    TYPE_OWNER = 1

    USER_TYPE_CHOICE = [
        (TYPE_OWNER, 'Empresa'),
        (TYPE_OWNER, 'Cliente')
    ]

    username = None
    email = models.EmailField('email', max_length=254, unique=True, blank=False)
    full_name = models.CharField('name', max_length=254, blank=False)
    type = models.PositiveSmallIntegerField('tipo', default=0, choices=USER_TYPE_CHOICE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


# Create your models here.
class Coworking(models.Model):
    STATUS_CHOICE = [
        ('ATIVO', 'Ativo'),
        ('PAGAMENTO_PENDENTE', 'Pagamento Pendente'),
        ('DESATIVADO', 'Desativado'),
    ]

    logo = models.ImageField(upload_to='imagens/coworking_logo')
    nome = models.CharField(max_length=150)
    descricao = models.TextField(max_length=255, blank=True, null=True)
    ativo = models.BooleanField(default=True)
    status = models.CharField(max_length=150, choices=STATUS_CHOICE)
    endereco = models.OneToOneField(Endereco, on_delete=models.PROTECT)
    cliente = models.ForeignKey(Cliente, related_name='endereco', on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Coworking'
        verbose_name_plural = 'Coworking\'s'
