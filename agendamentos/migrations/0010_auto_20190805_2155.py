# Generated by Django 2.2.3 on 2019-08-06 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0009_auto_20190805_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='horario_inicio',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='horario_termino',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]