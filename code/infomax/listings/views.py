from django.shortcuts import render,redirect
from django.http import HttpResponse
from listings.forms import client_form,auth_form
from listings.models import client
from listings import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Create your views here.
@login_required
def hello(request):
    return HttpResponse("<h1>Hllo</h1>")

@login_required()
def create_client(request):
    if request.method == 'POST':
        form = client_form(request.POST)
        if form.is_valid():
            client = form.save()
            return redirect('bravo/', views.bravo)
        
    else :
        form = client_form()

        return render(request,'listings/client_create.html',{'form' : form})

        
def bravo(request):
    return HttpResponse("<h1>Bravo</h1>")

def login(request):
    if request.method == 'POST':
        form = auth_form(request.POST)

        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request ,username=username,password = password)
            if user is not None:
                login(request,user)
                return redirect('/bravo/', views.bravo)
            
        else : 
            return redirect('/bravo/', views.bravo)
        
    else :
        form = auth_form()

        return render(request,'users/login.html',{'form' : form})
