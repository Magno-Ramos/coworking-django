# Generated by Django 2.2.3 on 2019-07-26 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salas', '0004_sala_coworking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sala',
            name='coworking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Coworking'),
        ),
    ]