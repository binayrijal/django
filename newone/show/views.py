from django.shortcuts import render
from django.http import HttpResponse
from .models import show

# Create your views here.
def home(request):
     
     return render(request,'index.html')


def submitted(request):
     name=request.POST['name']
     address=request.POST['address']
     email=request.POST['email']
     c=show()
     c.names="binay"
     c.addresss="hasanapur"
     c.emails="bin@gmail.com"
     c.rollnum=4

     return render(request,'show.html',{"name":name,"address":address,"email":email,"c":c})  