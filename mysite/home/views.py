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
            servicesID=form.cleaned_data['serviceID']
            #needsID=form.cleaned_data['needsID']
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

@csrf_protect
def index(request):
    form = HomeForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            #needsID=form.cleaned_data['needsID']
            service = CustomerService.objects.get(pk=request.user.customer.customerservice.id)
            service.needsID = form.cleaned_data['needsID']
            service.save()
            #newNeeds = request.user.customer.customerservice.objects.get(needsID = needsID)
            #newNeeds = form.cleaned_data['needsID']
            #newNeeds.save()
            #needsID=form.cleaned_data['needsID']
            #newNeeds = CustomerService.objects.updateNeeds(needsID)
            #newNeeds.save()
            return HttpResponseRedirect('job_post/')
        else:
            print(form.errors)
            print(form.cleaned_data)
            return HttpResponseRedirect('job_post/')
    return render(request, 'home/home.html', {'form': form})

#def needs_success(request):
 #   return render(request, 'home/job_post.html')
    
def faq(request):
    return render(request, 'home/faq.html')
    
def tos(request):
    return render(request, 'home/tos.html')
    
def contact(request):
    return render(request, 'home/contact.html')

def Post_list(request):
    if request.user.is_authenticated():
        #queryset_list = CustomerService.objects.all()
        queryset_list = CustomerService.objects.all()
        
        #user = CustomerService.objects.get(pk=request.user.customer.id)
        service = request.user.customer.customerservice.servicesID.split(", ")
        need = request.user.customer.customerservice.needsID.split(", ")
        zip = request.user.customer.zipCode
        customers_list = CustomerService.objects.all()
        matchedUsers_list = customers_list.filter(customer__zipCode = zip)
        print(need)
        print(service)
                
        return render(request, 'home/job_post.html', {'object_list': matchedUsers_list})
    # queryset_list = CustomerService.objects.all()
    # paginator = Paginator(queryset_list, 1)

    # page = request.GET.get('page', 1)
    # try:
        # queryset = paginator.page(page)
    # except PageNotAnInteger:
        # # If page is not an integer, deliver first page.
        # queryset = paginator.page(1)
    # except EmptyPage:
        # # If page is out of range (e.g. 9999), deliver last page of results.
        # queryset = paginator.page(paginator.num_pages)
    
    else:
        queryset_list = CustomerService.objects.all()
        return render(request, 'home/job_post.html', {'object_list': queryset_list})
    