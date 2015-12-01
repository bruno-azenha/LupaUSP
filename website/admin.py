from django.contrib import admin
from .models import DataFile, Periodo, Unidade, Funcao, Funcionario
# Register your models here.
admin.site.register(DataFile)
admin.site.register(Periodo)
admin.site.register(Unidade)
admin.site.register(Funcao)
admin.site.register(Funcionario)
