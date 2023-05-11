from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):

     return render(request,'index.html')
def submitted(request):
     name=request.POST['name']
     address=request.POST['address']
     email=request.POST['email']
     return render(request,'show.html',{"name":name},{"address":address},{"email":email})