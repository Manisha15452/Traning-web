# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import ContactForm,AssignmentForm
from .models import Contact,Ass,Assignment1
from django.db.models.fields import Field
from django.shortcuts import render
from django.shortcuts import render,render_to_response
from django.utils import timezone
from django.shortcuts import HttpResponseRedirect,HttpResponse
from .models import Mywebpage,UserProfileInfo,UserLogin
from .forms import UserForm,UserProfileInfoForm,User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage


def mywebpageview(request):
    return render(request,'home.html')

def index(request):
    return render(request,'index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
#
# def registration(request):
#     registered = False
#     if request.method == 'POST':
#         user_form = UserForm(data=request.POST)
#         profile_form = UserProfileInfoForm(data=request.POST)
#         if user_form.is_valid() and profile_form.is_valid():
#             user = user_form.save()
#             user.set_password(user.password)
#             user.save()
#             profile = profile_form.save(commit=False)
#             profile.user = user
#             if 'profile_pic' in request.FILES:
#                 print('found it')
#                 profile.profile_pic = request.FILES['profile_pic']
#             profile.save()
#             registered = True
#         else:
#             print(user_form.errors,profile_form.errors)
#     else:
#         user_form = UserForm()
#         profile_form = UserProfileInfoForm()
#     return render(request,'registration.html',
#                           {'user_form':user_form,
#                            'profile_form':profile_form,
#                            'registered':registered})

def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'user_login.html', {})


@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/contact/')
    else:
       form = ContactForm
       show = Contact.objects.all()
       print (show)
    return render(request,'contact.html', {'form':form}, {'details':show})

@login_required
def course(request):
    return render(request,'course.html')
@login_required
def aboutus(request):
    return render(request,'aboutus.html')
@login_required
def ass(request):
    if request.method == 'POST' and request.FILES['myfile']:
        form = AssignmentForm(request.POST)
        if form.is_valid():
            # form.save()
            name = form.cleaned_data.get('TraineeName')
            assignmentname = form.cleaned_data.get('AssignmentName')
            course = form.cleaned_data.get('CourseName')
            body = {'Name': name, 'AssignmentName': assignmentname ,'Unit': course},

            email = EmailMessage(
                'Assignment Form',
                str(body),
                to=['manishavenagandula@gmail.com']
            )
            email.send()
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            fs.save(myfile.name, myfile)
            messages.success(request, 'Successfully Uploaded! Admin will review the task. Thank You!')
        return HttpResponseRedirect('/assignment/')
    else:
        form = AssignmentForm()
        info = Ass.objects.filter(Email=request.user.email)
    return render(request, 'assignment.html', {'form': form, 'details': info})

def html(request):
    return render(request,'html.html')
def css(request):
    return render(request,'css.html')
def js(request):
    return render(request,'js.html')
def jquery(request):
    return render(request,'jquery.html')
def python(request):
    return render(request,'python.html')
def django(request):
    return render(request,'django.html')
def ebs(request):
    return render(request,'ebs.html')
def apex(request):
    return render(request,'apex.html')
def plsql(request):
    return render(request,'plsql.html')
