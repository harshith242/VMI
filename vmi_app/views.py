from django.shortcuts import render
from django.http import HttpResponse
from vmi_app.algo import model_vmi

# Create your views here.
def index(request):
	return render(request,'index.html')

def shop(request):
	return render(request,'shop.html')

def contact(request):
	return render(request,'contact.html')

def login_register(request):
	return render(request,'login-register.html')

def single_portfolio(request):
	return render(request,'single-portfolio.html')

def customer_review(request):
	return render(request,'customer-review.html')

def blog_details(request):
	return render(request,'index.html')

def vmi(request):
	if request.GET.get('vmi_opt'):
		opt=request.GET.get('vmi_opt')
		print('oapflsp:',opt)
		vmi_f=model_vmi(opt)
		print ('VMIIIIIII:',vmi_f)
		return render(request,'vmi.html',{'vmi':vmi_f})
	return render(request,'vmi.html',{})