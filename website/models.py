from django.db import models
from decimal import *

MONTH_CHOICES = (
	(1, 'Janeiro'),
	(2, 'Fevereiro'),
	(3, 'Março'),
	(4, 'Abril'),
	(5, 'Maio'),
	(6, 'Junho'),
	(7, 'Julho'),
	(8, 'Agosto'),
	(9, 'Setembro'),
	(10, 'Outubro'),
	(11, 'Novembro'),
	(12, 'Dezembro'),
)

# Create your models here.

# Data File
class DataFile(models.Model):
	ano = models.IntegerField()
	mes = models.IntegerField(choices=MONTH_CHOICES)
	active = models.BooleanField(default=False)
	dataFile = models.FileField(upload_to='dataFiles/')

	class Meta:
		unique_together = ('mes', 'ano')

# Período
class Periodo(models.Model):
	mes = models.IntegerField(choices=MONTH_CHOICES) # January is 1 - December is 12
	ano = models.IntegerField()
	totalFuncionarios = models.IntegerField(default=0)
	totalGastos = models.DecimalField(max_digits=14, decimal_places=2, default=Decimal('0.00'))

	class Meta:
		unique_together = ('mes', 'ano')

# Unidade
class Unidade(models.Model):
	unidade = models.CharField(max_length=25)
	totalFuncionarios = models.IntegerField(default=0)
	totalGastos = models.DecimalField(max_digits=14, decimal_places=2, default=Decimal('0.00'))
	periodo = models.ForeignKey('Periodo')

	class Meta:
		unique_together = ('unidade', 'periodo')

# Função 
class Funcao(models.Model):
	funcao = models.CharField(max_length=100)
	totalFuncionarios = models.IntegerField(default=0)
	totalGastos = models.DecimalField(max_digits=14, decimal_places=2, default=Decimal('0.00'))
	periodo = models.ForeignKey('Periodo')

	class Meta:
		unique_together = ('funcao', 'periodo')

# Funcionario
class Funcionario(models.Model):
	nome = 	models.CharField(max_length=100)
	departamento = models.CharField(max_length=200)
	jornada = models.CharField(max_length=25)
	categoria = models.CharField(max_length=25)
	classe = models.CharField(max_length=25)
	ref_ms = models.CharField(max_length=10)
	funcao_estrutura = models.CharField(max_length=100)
	tempo_usp = models.IntegerField()
	parcelas_eventuais = models.DecimalField(max_digits=14, decimal_places=2)
	salario_bruto = models.DecimalField(max_digits=14, decimal_places=2)
	salario_liquido = models.DecimalField(max_digits=14, decimal_places=2)

	unidade = models.ForeignKey('Unidade')
	funcao = models.ForeignKey('Funcao')
	periodo = models.ForeignKey('Periodo')










