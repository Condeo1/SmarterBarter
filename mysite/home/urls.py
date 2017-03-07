from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^tos/$', views.tos, name='tos'),
    
    url(r'^login/$', views.login, name='login'),
    url(r'^contact/$', views.contact, name='contact'),
]
