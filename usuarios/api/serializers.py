from rest_framework.serializers import ModelSerializer
from usuarios.models import Usuario
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class UsuarioSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Usuario
        fields = ['id', 'user', 'firebase_id']

    def to_representation(self, instance):
        id = instance.id
        firebase_id = instance.firebase_id
        username = instance.user.username
        first_name = instance.user.first_name
        last_name = instance.user.last_name
        email = instance.user.email

        nome = username

        if first_name:
            nome = first_name

        return {'id': id, 'nome': nome, 'sobrenome': last_name, 'email': email, 'firebase_id': firebase_id}
