from django.conf.urls import url, include
from django.contrib.auth.views import login
from django.views.generic import *
from . import views
from home.models import *
from home.views import *


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^tos/$', views.tos, name='tos'),
    url(r'^job_post/$', ListView.as_view(queryset = Customer.objects.all(), template_name = 'home/job_post.html')),
    url(r'^login/$', login, name='login'),
    url(r'^contact/$', views.contact, name='contact'),
    #url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^accounts/login/$', login), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^home/success/$', register_success), 
]
