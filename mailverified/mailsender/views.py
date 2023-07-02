from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if User.objects.filter(username=username).first():
            messages.success(request,'username taken')
            return redirect('/register')
        if User.objects.filter(email=email).first():
            messages.success(request,'email is already exist')
            return redirect('/register')
        user_obj=User.objects.create(username=username,email=email)
        user_obj.set_password(password)
        user_obj.save()
        auth_token=str(uuid.uuid4())
        profile_obj=Profile.objects.create(user=user_obj,auth_token=auth_token)
        profile_obj.save()
        send_Email(email,auth_token)
        return redirect('/token')

        
    return render(request,'register.html')


def send_Email(email,token):
    subject='this email for verification your credentials'
    body=f'hi click the given link http://127.0.0.1:8000/verify/{token}'
    email_from= settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject,body,email_from,recipient_list)


def token(request):
    return render(request,'token.html')


def success(request):
    return render(request,'success.html')

def verify(request,auth_token):
    profile_obj=Profile.objects.filter(auth_token=auth_token).first()
    if profile_obj:
     if profile_obj.is_verified:
         messages.success(request,'you are already verified')
         return redirect(request,'home.html')
     else:
      profile_obj.is_verified=True
      profile_obj.save()
      messages.success(request,'email is verified')
      return render(request,'home.html')
    else:
     return render(request,'error.html')