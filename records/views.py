from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request):
	return HttpResponse("Welcome home")


def record(request, patient_id):
	record_list = Patient.objects.order_by('-date_registered')[:10]
	context = {
				'record_list':record_list,
	}
	return render(request, 'records/index.html', context)