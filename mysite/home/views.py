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
 
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables =  RequestContext(request, {
    'form': form,
})
 
    return render_to_response(
    'home/register.html',
    variables,
    )
 
def register_success(request):
    return render_to_response(
    'home/success.html',
    )
 
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
    