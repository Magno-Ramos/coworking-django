# Generated by Django 2.2.3 on 2019-07-27 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coworking',
            name='cliente',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.PROTECT, to='clientes.Cliente'),
        ),
    ]
