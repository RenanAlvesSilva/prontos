# Generated by Django 5.0.7 on 2024-07-30 00:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionarios',
            name='unidade',
            field=models.ForeignKey(default='Selecione a Unidade', on_delete=django.db.models.deletion.CASCADE, related_name='Unidades', to='Adm.unidades'),
        ),
    ]
