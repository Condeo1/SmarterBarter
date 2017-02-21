from django.shortcuts import render

def index(request):
    return render(request, 'home/home.html')
    
def faq(request):
    return render(request, 'home/faq.html')
    
def tos(request):
    return render(request, 'home/tos.html')
    
def contact(request):
    return render(request, 'home/contact.html')