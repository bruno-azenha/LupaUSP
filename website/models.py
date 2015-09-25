from django.db import models

# Create your models here.

class Funcionario(models.Model):
	nome = models.Charfield(max_length=100)
	unidade = models.Charfield(max_length=50)
	departamento = models.Charfield(max_length=100)
	jornada = models.Charfield(max_length=50)
	models.Charfield(max_length=100)
	classe = models.Charfield(max_length=50)
	ref_MS = models.Charfield(max_length=10)
	funcao = models.Charfield(max_length=100)
	funcaoEstrutura = models.Charfield(max_length=100)
	tempoUSP = models.Integerfield()

	# Aqui esta o dinheiro
	parcelasEventuais = models.DecimalField(max_digits=8, 
											decimal_places=2)
	salario = models.DecimalField(max_digits=8, decimal_places=2)
	liquido = models.DecimalField(max_digits=8, decimal_places=2)




