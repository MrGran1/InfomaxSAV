from django.shortcuts import render,redirect
from django.http import HttpResponse
from listings.forms import client_form, user_form
from listings.models import client
from listings import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm 

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
            client = form.save()
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
                return redirect(request.GET.get('next'))
        
    else :
        form = AuthenticationForm()

    return render(request,'users/login.html',{'form' : form})


def logout_view(request):
    logout(request)
    return redirect(HOME)

@login_required
def create_user(request):
    if request.method == 'POST':
        form = user_form(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/home/', views.home)
        
    else :
        form = user_form()

    return render(request,'listings/create_user.html',{'form' : form})

