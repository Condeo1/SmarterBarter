from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.views.generic import View
from home.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from home.models import Customer, CustomerService
 
@csrf_protect
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['id_userName'],
            password=form.cleaned_data['id_password1'],
            email=form.cleaned_data['email'],
            first_name = form.cleaned_data['firstName'],
            last_name = form.cleaned_data['lastName']
            )
            
            customer = Customer.objects.makeCustomer(
            user=user,
            zipCode=form.cleaned_data['zipCode'],
            bio = form.cleaned_data['bio']
            )
            customer.save()
            
            services = CustomerService.objects.makeCustomerService(
            customer=customer,
            servicesID=form.cleaned_data['serviceID'],
            needsID = ""
            )
            services.save()
            
            return HttpResponseRedirect('/home/success')
        else:
            print(form.errors)
            print(form.cleaned_data)
            form = RegistrationForm()
 
    return render(request, 'home/register.html', {'form': form})
 
def register_success(request):
    return render(request, 'home/success.html')
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
#@login_required
#def home(request):
 #   return render_to_response(
  #  'home.html',
   # { 'user': request.user }
   # )

def index(request):
    return render(request, 'home/home.html')
    
def faq(request):
    return render(request, 'home/faq.html')
    
def tos(request):
    return render(request, 'home/tos.html')
    
def contact(request):
    return render(request, 'home/contact.html')

def job_post(request):
    return render(request, 'home/job_post.html')
    