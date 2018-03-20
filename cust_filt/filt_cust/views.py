from django.shortcuts import render
from .models import *
from .filters import CustomerFilter
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
	filter = CustomerFilter(request.GET, queryset=Customer.objects.all())
	customer = filter.qs
	context = {'filter':filter,
				'customer':customer,
				}
	return render(request,'filt_cust/home.html',context)

def listall(request):
	return render(request,'filt_cust/listall.html')	
