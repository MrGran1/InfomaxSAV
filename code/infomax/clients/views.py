from django.shortcuts import render
from django.http import HttpResponse
from clients.models import clients

# Create your views here.
def hello(request):
    clientss = clients.objects.all()
    return render(request,'clients/hello.html',{'clientss' : clientss})