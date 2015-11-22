from django.db import models

# Create your models here.

# Ano
class Ano(models.Model):
	ano = models.IntegerField(unique=True)
	totalGastos = models.DecimalField(max_digits=14, decimal_places=2)

# Mês
class Mes(models.Model):

	mes = models.IntegerField() # January is 1 - December is 12
	ano = models.ForeignKey('Ano')
	totalFuncionarios = models.IntegerField(default=0)
	totalGastos = models.DecimalField(max_digits=14, decimal_places=2)

	class Meta:
		unique_together = ('mes', 'ano')

# Funcionario
class Funcionario(models.Model):
	nome = 	models.CharField(max_length=100)
	unidade = models.CharField(max_length=25)
	departamento = models.CharField(max_length=100)
	jornada = models.CharField(max_length=25)
	categoria = models.CharField(max_length=25)
	classe = models.CharField(max_length=25)
	ref_ms = models.CharField(max_length=10)
	funcao = models.CharField(max_length=100)
	funcao_estrutura = models.CharField(max_length=100)
	tempo_usp = models.IntegerField()
	parcelas_eventuais = models.DecimalField(max_digits=14, decimal_places=2)
	salario_bruto = models.DecimalField(max_digits=14, decimal_places=2)
	salario_liquido = models.DecimalField(max_digits=14, decimal_places=2)

	mes = models.ForeignKey('Mes')

	class Meta:
		unique_together = ('nome', 'mes')








