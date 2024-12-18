# Generated by Django 5.0.7 on 2024-09-23 22:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adm', '0010_alter_funcionarios_unidade_and_more'),
        ('Controle', '0019_alter_pontosaida_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atrasos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now_add=True, null=True)),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Adm.funcionarios')),
            ],
            options={
                'verbose_name': 'Atraso',
                'verbose_name_plural': 'Atraso',
                'db_table': 'Atrasos',
            },
        ),
    ]
