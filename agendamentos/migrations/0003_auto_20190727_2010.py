# Generated by Django 2.2.3 on 2019-07-27 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('agendamentos', '0002_auto_20190726_1139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agendamento',
            name='usuario',
        ),
        migrations.AddField(
            model_name='agendamento',
            name='solicitante',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='usuarios.Usuario'),
        ),
    ]
