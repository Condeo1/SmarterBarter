from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm

def index(request):
    return render(request, 'home/home.html')
    
def faq(request):
    return render(request, 'home/faq.html')
    
def tos(request):
    return render(request, 'home/tos.html')
    
def contact(request):
    return render(request, 'home/contact.html')

def login(request):
    return render(request, 'home/login.html')
    
class UserFormView(View):
    form_class = UserForm
    template_name = 'home/register.html'
    
    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
        
    #process form data
    def post(self, request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            
            #cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            
            #returns User objects if credentials are correct
            user = authenticate(username=username, password=password)
            
            if(user != None):
                if(user.is_active):
                    login(request, user)
                    return redirect('home/home.html')
                    
        return render(request, self.template_name, {'form': form})