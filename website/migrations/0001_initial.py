# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ano',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('ano', models.IntegerField(unique=True)),
                ('totalGastos', models.DecimalField(decimal_places=2, max_digits=14)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('unidade', models.CharField(max_length=25)),
                ('departamento', models.CharField(max_length=100)),
                ('jornada', models.CharField(max_length=25)),
                ('categoria', models.CharField(max_length=25)),
                ('classe', models.CharField(max_length=25)),
                ('ref_ms', models.CharField(max_length=10)),
                ('funcao', models.CharField(max_length=100)),
                ('funcao_estrutura', models.CharField(max_length=100)),
                ('tempo_usp', models.IntegerField()),
                ('parcelas_eventuais', models.DecimalField(decimal_places=2, max_digits=14)),
                ('salario_bruto', models.DecimalField(decimal_places=2, max_digits=14)),
                ('salario_liquido', models.DecimalField(decimal_places=2, max_digits=14)),
            ],
        ),
        migrations.CreateModel(
            name='Mes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('mes', models.IntegerField()),
                ('totalFuncionarios', models.IntegerField(default=0)),
                ('totalGastos', models.DecimalField(decimal_places=2, max_digits=14)),
                ('ano', models.ForeignKey(to='website.Ano')),
            ],
        ),
        migrations.AddField(
            model_name='funcionario',
            name='mes',
            field=models.ForeignKey(to='website.Mes'),
        ),
        migrations.AlterUniqueTogether(
            name='mes',
            unique_together=set([('mes', 'ano')]),
        ),
        migrations.AlterUniqueTogether(
            name='funcionario',
            unique_together=set([('nome', 'mes')]),
        ),
    ]
