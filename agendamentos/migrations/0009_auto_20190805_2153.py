# Generated by Django 2.2.3 on 2019-08-06 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0008_auto_20190805_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='horario_inicio',
            field=models.DateTimeField(),
        ),
    ]