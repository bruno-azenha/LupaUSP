# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.core.urlresolvers import reverse
from django.core.files import File
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
from decimal import *

from .models import *
from .forms import DataFileForm

@login_required
def addDataFile(request):
	# Handle file upload
	if request.method == 'POST':
		form = DataFileForm(request.POST, request.FILES)
		if form.is_valid():
			ano = form.cleaned_data['ano']
			mes = form.cleaned_data['mes']
			newDataFile = DataFile()
			newDataFile.ano = ano
			newDataFile.mes = mes
			newDataFile.dataFile = request.FILES['dataFile']	
			newDataFile.save()

			# Redirect to the document list after POST
			return HttpResponseRedirect(reverse('website.views.addDataFile'))
	else:
		form = DataFileForm()  # An empty, unbound form

	# Load documents for the list page
	dataFiles = DataFile.objects.all()

	# Render database_admin page with the documents and the form
	return render_to_response(
		'database_admin.html',
		{'dataFiles': dataFiles, 'form': form},
		context_instance=RequestContext(request)
	)

@login_required
def ConsolidateDataFiles (request):

	# First get all DataFile objects
	dataFiles = DataFile.objects.all()

	for df in dataFiles:
		
		# Verifies if df is already active
		if df.active == True:
			continue

		print("Consolidating datafile: Ano: {0}, Mês: {1}".format(df.ano, df.mes))


		# Creates Período entry
		periodoObj = Periodo(mes=df.mes, ano=df.ano)
		periodoObj.save()

		totalGastos = Decimal('0.00')
		totalFuncionarios = 0

		first = True;
		# Opens the data file
		f = df.dataFile.file
		for line in f:
			if first: 
				first = False
				continue
			newFuncionario = Funcionario()
			attributes = line.decode('utf8').split(';')

			# Sets all attributes according to data file
			newFuncionario.nome = attributes[0]
			newFuncionario.departamento = attributes[2]
			newFuncionario.jornada = attributes[3]
			newFuncionario.categoria = attributes[4]
			newFuncionario.classe = attributes[5]
			newFuncionario.ref_ms = attributes[6]
			newFuncionario.funcao_estrutura = attributes[8]
			newFuncionario.tempo_usp = int(attributes[9])
			newFuncionario.parcelas_eventuais = Decimal(attributes[10].replace(',', '.'))
			newFuncionario.salario_bruto = Decimal(attributes[11].replace(',', '.'))
			newFuncionario.salario_liquido = Decimal(attributes[12].replace(',', '.'))

			print("Added {}.".format(attributes[0]))

			# Set unidade
			try:
				unidadeObj = Unidade.objects.get(unidade=attributes[1], periodo=periodoObj)
			except ObjectDoesNotExist:
				unidadeObj = Unidade(unidade=attributes[1], periodo=periodoObj)

			# Set Funcao
			try:
				funcaoObj = Funcao.objects.get(funcao=attributes[7], periodo=periodoObj)
			except ObjectDoesNotExist:
				funcaoObj = Funcao(funcao=attributes[7], periodo=periodoObj)

			totalGastos += Decimal(attributes[10].replace(',', '.')) + Decimal(attributes[11].replace(',', '.'))
			totalFuncionarios += 1

			funcaoObj.totalFuncionarios += 1
			funcaoObj.totalGastos += Decimal(attributes[11].replace(',', '.'))
			funcaoObj.save()

			unidadeObj.totalFuncionarios += 1
			unidadeObj.totalGastos += Decimal(attributes[11].replace(',', '.'))
			unidadeObj.save()

			newFuncionario.unidade = unidadeObj
			newFuncionario.funcao = funcaoObj
			newFuncionario.periodo = periodoObj
			newFuncionario.save()

		f.close()

		df.active = True
		df.save()

		periodoObj.totalGastos = totalGastos
		periodoObj.totalFuncionarios = totalFuncionarios
		periodoObj.save()


def homePage(request):
	# Render database_admin page with the documents and the form
	return render_to_response(
		'home.html',
		{},
		context_instance=RequestContext(request)
	)

def getData(request):
	response = serializers.serialize("json", Periodo.objects.all())
	return JsonResponse(response, safe=False)




	
