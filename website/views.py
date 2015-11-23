# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.files import File
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

from .models import DataFile, Ano, Mes, Funcionario
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
	2+3


"""
	# First get all DataFile obsjects
	dataFiles = DataFile.obsjects.all()

	for df in dataFiles:

		# Verifies if df is already active
		if df.active == True:
			continue

		# Gets or Creates Year entry
		(anoObj, created) = Ano.objects.get_or_create(ano=df.ano, defaults={'ano': df.ano})

		# Creates Month entry
		mesObj = Mes()
		mesObj.mes = df.mes
		mesObj.ano = df.ano
		mesObj.save()

		totalGastos = 0
		totalFuncionarios = 0

		first = True;
		# Opens the data file
		f = newDataFile.dataFile.file
		for line in f:
			if first: 
				first = False
				continue
			newFuncionario = Funcionario()
			attributes = line.decode('utf8').split(';')

			# Sets all attributes according to data file
			newFuncionario.nome = attributes[0]
			newFuncionario.unidade = attributes[1]
			newFuncionario.departamento = attributes[2]
			newFuncionario.jornada = attributes[3]
			newFuncionario.categoria = attributes[4]
			newFuncionario.classe = attributes[5]
			newFuncionario.ref_ms = attributes[6]
			newFuncionario.funcao = attributes[7]
			newFuncionario.funcao_estrutura = attributes[8]
			newFuncionario.tempo_usp = int(attributes[9])
			newFuncionario.parcelas_eventuais = float(attributes[10].replace(',', '.'))
			newFuncionario.salario_bruto = float(attributes[11].replace(',', '.'))
			newFuncionario.salario_liquido = float(attributes[12].replace(',', '.'))

			totalGastos += float(attributes[10].replace(',', '.')) + float(attributes[11].replace(',', '.'))
			totalFuncionarios += 1

			newFuncionario.mes = mesObj

			newFuncionario.save()

		f.close()

		mesObj.totalGastos = totalGastos
		mesObj.totalFuncionarios = totalFuncionarios
		mesObj.save()

		anoObj.totalGastos += totalGastos
		anoObj.save()

		"""

	
