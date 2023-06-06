from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth 

# Create your views here.
def login(request):
  if request.method == 'POST':
     username=request.POST['username']
     password=request.POST['password']
     user=auth.authenticate(username=username,password=password)
     if user is not None:
      auth.login(request,user)
      return redirect('/')
     else :
      messages.info(request,'invalid credentials')
      return redirect('login')
  else:
     return render(request,'login.html')

  
      

#register view parts
def Register(request):
  if request.method=='POST':
      username=request.POST['username']
      first_name=request.POST['first-name']
      last_name=request.POST['last-name']
      email=request.POST['email']
      password1=request.POST['pass1']
      password2=request.POST['pass2']
      if password1==password2:
        if User.objects.filter(username=username).exists():
          messages.info(request,['user name is already exist','user name is required'])
          return redirect('Register')
        elif User.objects.filter(email=email).exists():
          messages.info(request,'email is already exist')
          return redirect('Register')
        else :
         user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
         user.save();
         return redirect('login')
         
         
        
      else:
        messages.info(request,'password doesnot match')
        return redirect('Register')

      
  else:
     
     return render(request,'Register.html')
     
  



#logout part here 
def logout(request):
 auth.logout(request)
 return redirect('/')



def edit(request):
 if request.method=='POST':
   return render(request,'Register')

