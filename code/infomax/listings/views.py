from django.shortcuts import render,redirect
from django.http import HttpResponse
from listings.forms import client_form, user_form, afficher_client_form,form_modif_tech
from listings.models import depot,CustomUser
from listings import views
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm 
from datetime import date
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from reportlab.pdfgen import canvas
import io
from django.http import FileResponse
from .forms import form_input

HOME = '/home'

@login_required
def create_pdf(request,id):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    depot_var = depot.objects.get(numero_depot=id)
    marge = 780
    p.drawString(250, 800, "Bon de dépot")
    for field in str(depot_var._meta.get_fields):
        marge -= 20
        p.drawString(100, marge, str(field))

    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="hello.pdf")


# Create your views here.
@login_required
def hello(request):
    return HttpResponse("<h1>Hllo</h1>")


@login_required()
def create_client(request):
    if request.method == 'POST':
        form = form_input(request.POST)
        if form.is_valid():
            print("oui")
            depot = form.save(commit = False)
            depot.first_name_seller = request.user.first_name
            depot.last_name_seller = request.user.last_name

            today = date.today()    
            depot.date = today.strftime("%Y-%m-%d")
            depot.save()
            "Envoie mail reception"
            subject = 'Test Email'
            message = 'Le colis est pris en charge par nos équipes'
            from_email = 'tigran.wattrelos@outlook.fr'
            recipient_list = [depot.email]
            send_mail(subject, message, from_email, recipient_list)
            "Print un message comme quoi c'est bien passé"
            return redirect(f'/pdf/{depot.numero_depot}')
        else : 
            print(form.errors)

    else :
        form = form_input()

    return render(request,'listings/create_depot.html',{'form' : form})

def home(request):
    return render(request,'listings/home.html')

def login_view(request):
    if request.method == 'POST':
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

### Vue pour chercher des clients######
@login_required
def afficher_client(request):
    if request.method == 'POST':
        form = afficher_client_form(request.POST)
        if form.is_valid():
            

            
            name = form.cleaned_data['name']
            ref = form.cleaned_data['ref_commande']
            first_name = form.cleaned_data['first_name']
            clients = depot.objects.filter(ref_commande__contains = ref,name__contains = name, first_name__contains = first_name)
        
        ### Si un champs est renseigné et le client existe ########
            if ((len(name)!=0 or len(ref)!=0 or len(first_name)!=0)):
                return render(request,"listings/afficher_depot.html",{"form":form,'clients':clients,})

        ### Si aucun champ n'est renseigné ### 
            else :
                return render(request,"listings/afficher_depot_erreur_champs.html",{"form":form})
        ### Sinon si le client n'existe pas ###           
    else :
        form = afficher_client_form()
    
    return render(request,"listings/recherche_depot.html",{"form":form})
@login_required
def modif_depot(request,id):
    depot_var = depot.objects.get(numero_depot=id)

    if request.method == 'POST':
        form = client_form(request.POST,instance=depot_var)
        if form.is_valid():
            statut_form = form.cleaned_data['statut']

###Envoi d'email
            if  statut_form =='TR' and  depot_var.mail_envoyee == 'RC' :
                subject = 'Test Email'
                message = 'Le colis est en traitement par les techniciens'
                from_email = 'tigran.wattrelos@outlook.fr'
                recipient_list = [depot_var.email]
                send_mail(subject, message, from_email, recipient_list)
                depot_var.mail_envoyee = 'TR'


            elif statut_form =='TM' and  (depot_var.mail_envoyee == 'RC' or depot_var.mail_envoyee == 'TR'):
                subject = 'Test Email'
                message = 'Le colis est pret à etre récuperer'
                from_email = 'tigran.wattrelos@outlook.fr'
                recipient_list = [depot_var.email]
                send_mail(subject, message, from_email, recipient_list)
                depot_var.mail_envoyee = 'TM'

            form.save()
    else:
        form = client_form(instance=depot_var)
   
    return render (request,'listings/create_user.html',{'form':form})


def depot_tech(request,id):
    depot_var = depot.objects.get(numero_depot=id)
    if request.method == 'POST':
        form = modif_client_form_tec(request.POST,instance=depot_var)    
        form.save()

    else:
        form = modif_client_form_tec(instance=depot_var)

    return render (request,'listings/interface_tech.html',{'form':form})


def afficher_user(request):
    users = CustomUser.objects.all()
    print(users)
    return render(request,"listings/afficher_users.html",{"users" : users})

def supprimer_user(request, username):
    user_to_del = CustomUser.objects.get(username = username)
    if request.method == 'POST':
        # supprimer le user de la base de données
        user_to_del.delete()
        # rediriger vers le home
        return redirect('/home')

    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement

    return render(request,
                    'listings/delete_user.html',
                    {'user': user_to_del})
