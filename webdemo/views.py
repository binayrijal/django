from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Team,contact
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def index(request):
   Tem1=Team.objects.all()
   return render(request,'index.html',{'Tem1':Tem1})

#contact section is here
def cont(request):
  if request.method=='POST':
    name=request.POST['name']
    email=request.POST['email']
    message=request.POST['message']
    subject=request.POST['subject']
    listofform=[name,email,message,subject]
    if listofform:
      user=contact(name=name,email=email,subject=subject,message=message)
      user.save();
      messages.info(request,'thanks for your concern')
      
      return HttpResponse('thanks for the submission')
      
      
      
    else:
      messages.info('email and message is required')
      print('something is missing')
      return render(request,'/')
  else:
    print('this is else')
    return render(request,'/')
    