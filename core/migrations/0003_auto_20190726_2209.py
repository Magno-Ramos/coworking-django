# Generated by Django 2.2.3 on 2019-07-27 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_coworking_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coworking',
            name='cliente',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='clientes.Cliente'),
        ),
    ]