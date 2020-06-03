from django.conf.urls import url
from .models import Mywebpage, UserProfileInfo,UserLogin,Ass,Assignment1
from django.shortcuts import HttpResponse
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.mywebpageview, name='home'),
    url(r'^user_login/', views.userlogin, name='user_login'),
    url(r'^index/', views.index, name='index'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^course/', views.course, name='course'),
    url(r'^about/',views.aboutus,name='aboutus'),
    url(r'^assignment/$',views.ass,name='assignment'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^html/$', views.html, name='html'),
    url(r'^css/$', views.css, name='css'),
    url(r'^js/$', views.js, name='js'),
    url(r'^jquery/$', views.jquery, name='jquery'),
    url(r'^python/$', views.python, name='python'),
    url(r'^django/$', views.django, name='django'),
    url(r'^plsql/$', views.plsql, name='plsql'),
    url(r'^ebs/$', views.ebs, name='ebs'),
    url(r'^apex/$', views.apex, name='apex'),
]
