# -*- coding: utf-8 -*-

from django.forms import ModelForm
from .models import DataFile

class DataFileForm(ModelForm):
	class Meta:
		model = DataFile
		fields = ['ano', 'mes', 'dataFile']
