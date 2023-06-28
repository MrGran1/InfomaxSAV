from django.shortcuts import render,redirect
from django.http import HttpResponse
from listings.forms import client_form, user_form
from listings.models import depot
from listings import views
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm 
from datetime import date
HOME = '/home'

# Create your views here.
@login_required
def hello(request):
    return HttpResponse("<h1>Hllo</h1>")


@login_required()
def create_client(request):
    if request.method == 'POST':
        form = client_form(request.POST)
        if form.is_valid():
            depot = form.save(commit = False)
            depot.first_name_seller = request.user.first_name
            depot.last_name_seller = request.user.last_name


            today = date.today()    
            depot.date = today.strftime("%Y-%m-%d")
            depot.save()
            "Envoie mail reception"
            "Print un message comme quoi c'est bien passé"
            return redirect(HOME)
        
    else :
        form = client_form()

    return render(request,'listings/client_create.html',{'form' : form})

def home(request):
    return render(request,'listings/home.html')

def login_view(request):
    if request.method == 'POST':
        #form = auth_form(request.POST)
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request ,username = username,password = password)
            if user is not None:
                login(request,user)
                try:
                    return redirect(request.GET.get('next'))
                except:
                    return redirect('/home')
        
    else :
        form = AuthenticationForm()

    return render(request,'users/login.html',{'form' : form})


def logout_view(request):
    logout(request)
    return redirect(HOME)

def check_superuser(user):
    return user.is_superuser

@login_required
@user_passes_test(check_superuser)
def create_user(request):
    if request.method == 'POST':
        form = user_form(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            # is_super = form.cleaned_data.get('is_superuser')
            # first_name = form.cleaned_data.get('first_name')
            # last_name = form.cleaned_data.get('last_name')

            user = form.save(commit = False)
            user.username = user.first_name + "." + user.last_name
            user.set_password(password)
            user.save()

            return redirect('/home/', views.home)
        
    else :
        form = user_form()

    return render(request,'listings/create_user.html',{'form' : form})

def afficher_client(request):
    clients = depot.objects.filter(first_name = 'Tigran')
    return render(request,"listings/afficher_client.html",{'client' : clients[0]})

