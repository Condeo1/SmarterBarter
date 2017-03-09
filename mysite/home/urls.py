from django.conf.urls import url, include
from django.contrib.auth.views import login
from . import views
from home.views import *


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^tos/$', views.tos, name='tos'),
    url(r'^job_post/$', views.job_post, name='job_post'),
    url(r'^login/$', login, name='login'),
    url(r'^contact/$', views.contact, name='contact'),
    #url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^accounts/login/$', login), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
]
