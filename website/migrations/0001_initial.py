# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('unidade', models.CharField(max_length=50)),
                ('departamento', models.CharField(max_length=100)),
                ('jornada', models.CharField(max_length=50)),
                ('classe', models.CharField(max_length=50)),
                ('ref_MS', models.CharField(max_length=10)),
                ('funcao', models.CharField(max_length=100)),
                ('funcaoEstrutura', models.CharField(max_length=100)),
                ('tempoUSP', models.IntegerField()),
                ('parcelasEventuais', models.DecimalField(decimal_places=2, max_digits=8)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=8)),
                ('liquido', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
