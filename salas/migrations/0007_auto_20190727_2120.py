# Generated by Django 2.2.3 on 2019-07-28 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salas', '0006_remove_sala_preco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotossala',
            name='sala',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fotos', to='salas.Sala'),
        ),
    ]
