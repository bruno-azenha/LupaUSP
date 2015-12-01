from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^$', homePage, name='home'),
	url(r'^getData/', getData, name='getData'),
	url(r'^addData/$', addDataFile, name='addData'),
	url(r'^addData/Consolidate$', ConsolidateDataFiles, name='consolidateDataFiles'),
	url(r'^wealth/', wealth, name='wealth'),

)

