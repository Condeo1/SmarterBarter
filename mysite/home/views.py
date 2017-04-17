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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from functools import reduce
from django.db.models import Q
 
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
 


@csrf_protect
def index(request):
    form = HomeForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            service = CustomerService.objects.get(pk=request.user.customer.customerservice.id)
            service.needsID = form.cleaned_data['needsID']
            service.save()
            
            return HttpResponseRedirect('job_post/')
        else:
            print(form.errors)
            print(form.cleaned_data)
            return HttpResponseRedirect('job_post/')
    return render(request, 'home/home.html', {'form': form})


def faq(request):
    return render(request, 'home/faq.html')
    
def tos(request):
    return render(request, 'home/tos.html')
    
def contact(request):
    return render(request, 'home/contact.html')

def Post_list(request):
    if request.user.is_authenticated():
        queryset_list = CustomerService.objects.all()
        
        service = request.user.customer.customerservice.servicesID
        need = request.user.customer.customerservice.needsID
        need.lstrip('[')
        need.rstrip(']')
        need.split(", ")
        
        service.lstrip('[')
        service.rstrip(']')
        service.split(", ")
       
        zip = request.user.customer.zipCode
        customers_list = CustomerService.objects.all()
        matchedUsers_list = customers_list.filter(customer__zipCode = zip)
        matchedUsersTwo_list = matchedUsers_list
        matchedUsersThree_list = CustomerService.objects.none()
        serviceList = matchedUsersTwo_list.values_list('servicesID', flat=True)
     
        
        for x in need:
            for y in serviceList:
                if y.find(x):
                    matchedUsersThree_list=matchedUsersTwo_list.filter(y)
            
        
#        query=Q()
#        serviceList = matchedUsersTwo_list.values_list('servicesID', flat=True)
#        for service in serviceList:
#            query = query | Q(servicesID__contains=need)
#        matchedUsersTwo_list = matchedUsersTwo_list.filter(query)
        
        print(need)
        print(service)
        
        paginator = Paginator(matchedUsersThree_list, 4)
        page = request.GET.get('page', 1)
        
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
            
                
        return render(request, 'home/job_post.html', {'object_list': queryset})
    
    
    else:
        queryset_list = CustomerService.objects.all()
        paginator = Paginator(queryset_list, 4)
        page = request.GET.get('page', 1)

        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
            
        return render(request, 'home/job_post.html', {'object_list': queryset})
    

    