from django.shortcuts import render,redirect
from listings.forms import client_form, user_form, afficher_client_form,form_modif_tech,form_input,change_password_form
from listings.models import depot,CustomUser
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm 
from datetime import date
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django_renderpdf.views import PDFView
import json
from .forms import LoginForm
from django.contrib.auth.views import LoginView
from .utils import generate_password

#from .forms import form_input

HOME = '/home'
with open("./listings/configuration.json","r") as file:
    config = json.load(file)

def envoi_mail(liste_destinataire, subject, message):
    """ Envoie un mail à tout les destinataires avec l'objet et le message suivant """

    from_email = 'tigran.wattrelos@outlook.fr'  # Mettre le mail dans une variable d'environement
    recipient_list = liste_destinataire
    send_mail(subject, message, from_email, recipient_list)

                    
@login_required()
def create_depot(request):
    if request.method == 'POST':
        form = form_input(request.POST)
        if form.is_valid():
            client = depot(
            mode_envoi=form.cleaned_data['mode_envoi'],
            designation=form.cleaned_data['designation'],
            name=form.cleaned_data['nom'],
            first_name=form.cleaned_data['first_name'],
            telephone=form.cleaned_data['telephone'],
            email=form.cleaned_data['email'],
            mdp_windows=form.cleaned_data['mdp_windows'],
            probleme=form.cleaned_data['probleme'],
            ref_commande=form.cleaned_data['ref_commande'],
            carton = form.cleaned_data['carton'],
            alimentation = form.cleaned_data['alimentation'],
            reinitialisation = form.cleaned_data['reinitialisation']
            )

            print(client.mode_envoi[0])
            client.first_name_seller = request.user.first_name
            client.last_name_seller = request.user.last_name

            today = date.today()    
            client.date = today.strftime("%Y-%m-%d")

            client.save()

        # ------------   Envoie d'un mail à la création du dépot  -------------------
            objet_mail = config['mail']["objet_creation_depot"]
            message_mail = config['mail']["message_creation_depot"]

            envoi_mail([client.email],objet_mail, message_mail )
            return redirect(f'/pdf_interne/{client.numero_depot}')
        # ---------------------------------------------------------------------------

        else:
            print (form.errors)
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

def create_user_withform(request,form):
    """Crée un user grâce au formulaire"""
    email = form.cleaned_data.get('email')
    user_to_create = form.save(commit = False)
    user_to_create.username = user_to_create.first_name + "." + user_to_create.last_name
    user_to_create.email = email
    random_password = generate_password(14)
    user_to_create.set_password(random_password)

    send_mail(config['mail']['objet_creation_compte'], config['mail']["message_creation_compte"] + random_password,config['mail']['adresse_email'],[user_to_create.email])
    if not CustomUser.objects.filter(username = user_to_create.username).exists():
        user_to_create.save() 


@login_required
@user_passes_test(check_superuser)
def create_user(request):
    if request.method == 'POST':
        form = user_form(request.POST)
        if form.is_valid():
            create_user_withform(request,form)     
    else :
        form = user_form()

    users = CustomUser.objects.all()
    return render(request,'listings/create_user.html',{'form' : form,"users" : users,'edit':False})

@login_required
@user_passes_test(check_superuser)
def edit_user(request):
    # !! Fonction jamais testé !! # 
    # View pour gérer les utilisateurs (suppression, edition, création)
    if request.method == 'POST':
        form = user_form(request.POST) # Fromulaire pour le nouveau user

        if request.POST.get("username_to_suppr"):
            # Si l'on veut supprimer un user alors :
            username_to_suppr = request.POST.get("username_to_suppr")
            user_to_del = CustomUser.objects.get(username = username_to_suppr)
            user_to_del.delete()
        
        if request.POST.get("username_to_edit"):
            ## Si un user doit être modifié
            username_to_edit = request.POST.get("username_to_edit")
            user_to_edit = CustomUser.objects.get(username=username_to_edit)
            form_edition = user_form(request.POST,instance=user_to_edit)
            if form_edition.is_valid():
                form_edition.save()

        if form.is_valid():
                # Création d'un user si le formulaire de création est valide
                create_user_withform(request,form)

    # On retourne les formulaires vide pour les utiliser dans le html
    form = user_form()
    form_edition = user_form()
    users =  CustomUser.objects.all()
    return render (request,'listings/create_user.html',{'form' : form,"form_edition": form_edition,"users" : users})

@login_required
def change_password(request):
    """Différentes erreurs : 
    error_status
    402 = Wrong password
    403 = mauvaise correspondance des nouveaux password
    400 = Mot de passe bien changé
    401 = au départ avant de changer le mdp
    """
    if request.method == 'POST':
        form = change_password_form(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data.get('old_password')
            new_password = form.cleaned_data.get('new_password')
            double_check_password = form.cleaned_data.get('double_check_password')
            user = authenticate(username=request.user.username, password=old_password)
            if user is None:
                return render(request,'listings/change_password.html',{'form' : form,"error_status" : 402})

            elif new_password != double_check_password:
                return render(request,'listings/change_password.html',{'form' : form,"error_status" : 403})
            
            else:
                request.user.set_password(new_password)
                request.user.save()
                return render(request,'listings/change_password.html',{'form' : form, "error_status" : 400}) 
                
    else :
        form = change_password_form()
        return render(request,'listings/change_password.html',{'form' : form, "error_status" : 401})
    
def oubli_mdp(request):
    """ Change le mdp du user par un random et envoi ce mdp à l'admin
     !!! PAs fini !!!!!
       """
    new_mdp = generate_password(14)
    request.user.set_password(new_mdp)
    request.user.save()
    print("Nouveau mdp : ",new_mdp)
    send_mail(config['mail']['objet_mdp_oublie'],
              config['mail']['mail_mdp_oublie'],
              config['mail']['adresse_email'],
              config['mail']['mail_admin'])
    
### Vue pour chercher des clients######
@login_required
def afficher_client(request):
    """ Recherche les depots dans la base de données en fonction des champs renseigné par l'utilisateur, si aucun champs n'est renseigné, cela renvoie tout les clients"""
    if request.method == 'POST':
        form = afficher_client_form(request.POST)
        
        if form.is_valid():

            clients = depot.objects.all()
                    #On renseigne tout les champs du formulaire
            name = form.cleaned_data['name']
            ref = form.cleaned_data['ref_commande']
            first_name = form.cleaned_data['first_name']
            telephone = form.cleaned_data['telephone']
            email = form.cleaned_data['email']
            numero_depot = form.cleaned_data['numero_depot']

            clients = depot.objects.filter(ref_commande__contains = ref,name__contains = name, first_name__contains = first_name,telephone__contains = telephone, email__contains = email, numero_depot__contains = numero_depot)
        
        ### Si aucun clients n'est trouvé alors cela retourne toute la BD###           
    else:
        clients = depot.objects.all()
        form = afficher_client_form()
    
    return render(request,"listings/recherche_depot.html",{"form":form,'clients':clients,})

@login_required
def modif_depot(request,id):
    depot_var = depot.objects.get(numero_depot=id)

    if request.method == 'POST':
        form = client_form(request.POST,instance=depot_var)
        if form.is_valid():
            statut_form = depot_var.statut

            ###Envoi d'email
            if  statut_form =='TR' and  depot_var.mail_envoyee == 'RC' :
                subject = 'Test Email'
                message = config['email']['message_en_traitement']
                from_email = config['email']
                recipient_list = [depot_var.email]
                send_mail(subject, message, from_email, recipient_list)
                depot_var.mail_envoyee = 'TR'


            elif statut_form =='TM' and  (depot_var.mail_envoyee == 'RC' or depot_var.mail_envoyee == 'TR'):
                subject = 'Test Email'
                message = config['mail']['message_recuperation']
                from_email = config['mail']['adresse_email']
                recipient_list = [depot_var.email]
                send_mail(subject, message, from_email, recipient_list)
                depot_var.mail_envoyee = 'TM'

            form.save()
    else:
        form = client_form(instance=depot_var)
   
    return render (request,'listings/modif_depot.html',{'form':form, 'depot':depot_var})


def depot_tech(request,id):
    depot_var = depot.objects.get(numero_depot=id)
    if request.method == 'POST':
        form = form_modif_tech(request.POST,instance=depot_var)    
        form.save()

    else:
        form = form_modif_tech(instance=depot_var)

    return render (request,'listings/modif_tech.html',{'form':form, 'depot':depot_var})


def afficher_user(request):
    users = CustomUser.objects.all()
    return render(request,"listings/afficher_users.html",{"users" : users})

class PDF_interne(LoginRequiredMixin, PDFView):
    """Generate labels for some Shipments.

    A PDFView behaves pretty much like a TemplateView, so you can treat it as such.
    """
    template_name = 'listings/pdf_interne.html'

    def get_context_data(self, *args, **kwargs):
        """Pass some extra context to the template."""
        context = super().get_context_data(*args, **kwargs)
        depot_var = depot.objects.get(numero_depot=kwargs['id'])
        context['depot'] = depot_var

        return context

class PDF_client(LoginRequiredMixin, PDFView):
    template_name = 'listings/pdf_client.html'

    def get_context_data(self, *args, **kwargs):
        """Pass some extra context to the template."""
        context = super().get_context_data(*args, **kwargs)
        depot_var = depot.objects.get(numero_depot=kwargs['id'])
        context['depot'] = depot_var

        return context

def pdf_interne(request):
    return render(request,'pdf_interne.html')

class CustomLoginView(LoginView):
    form_class = LoginForm