from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def current_datetime(request):
	context = {}
	return render(request, 'database_admin.html', context)
