from django.db import models

# Create your models here.

class Funcionario(models.Model):
	nome = models.CharField(max_length=100)
	unidade = models.CharField(max_length=50)
	departamento = models.CharField(max_length=100)
	jornada = models.CharField(max_length=50)
	models.CharField(max_length=100)
	classe = models.CharField(max_length=50)
	ref_MS = models.CharField(max_length=10)
	funcao = models.CharField(max_length=100)
	funcaoEstrutura = models.CharField(max_length=100)
	tempoUSP = models.IntegerField()

	# Aqui esta o dinheiro
	parcelasEventuais = models.DecimalField(max_digits=8, 
											decimal_places=2)
	salario = models.DecimalField(max_digits=8, decimal_places=2)
	liquido = models.DecimalField(max_digits=8, decimal_places=2)




