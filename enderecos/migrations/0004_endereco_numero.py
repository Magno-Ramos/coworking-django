# Generated by Django 2.2.3 on 2019-07-26 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0003_auto_20190726_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='numero',
            field=models.IntegerField(default=0),
        ),
    ]