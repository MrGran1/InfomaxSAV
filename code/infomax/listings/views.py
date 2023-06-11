from django.shortcuts import render,redirect
from django.http import HttpResponse
from listings.forms import client_form
from listings.models import client
from listings import views

# Create your views here.

def hello(request):
    return HttpResponse("<h1>Hllo</h1>")

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