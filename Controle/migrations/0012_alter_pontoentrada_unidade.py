# Generated by Django 5.0.7 on 2024-08-25 01:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adm', '0009_funcionarios_usuario_alter_funcionarios_nome'),
        ('Controle', '0011_pontoentrada_unidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontoentrada',
            name='unidade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Adm.funcionarios'),
        ),
    ]