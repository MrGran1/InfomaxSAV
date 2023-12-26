from django import forms
from listings.models import depot,CustomUser
from .models import depot
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'custom-class-username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'custom-class-password'}))


class form_input(forms.TextInput):
        def __init__(self, *args, **kwargs):
            attrs={
                'class':'custom-input',

            }
            kwargs.setdefault('attrs', attrs)
            super().__init__(*args, **kwargs)


designation_choix = [
        ('', '---------'),
        ('PO', 'Laptop'),
        ('CO', 'Config'),
        ('AR', 'Article')
        
    ]

envoi_choix = [
        ('', '---------'),
        ('RE', 'Retrait'),
        ('EX', 'Expédition')
        
    ]

raison_retour_choix = [
        ('', '---------'),
        ('DF', 'Defaut montage'),
        ('DP', 'Defaut produit'),
        ('PS', 'Defaut systeme'),
        ('PU', 'Probleme utilisateur'),
        ('PT', 'Probleme transport'),
        ('PC', 'Probleme compatibilite')
    ]


class form_input(forms.Form):
    mode_envoi= forms.ChoiceField(choices=envoi_choix, widget=forms.Select(
        attrs={}))
        
    designation= forms.ChoiceField(choices=designation_choix, widget=forms.Select(
        attrs={'class':'designation'}))
        
    nom= forms.CharField(max_length=50, widget=forms.TextInput (
        attrs={'class':'nom'}))
        
    first_name= forms.CharField(max_length=50, widget=forms.TextInput (
        attrs={'class':'prenom'}))
        
    telephone= forms.CharField(max_length=50, widget=forms.TextInput (
        attrs={'class':'telephone'}))
        
    email= forms.EmailField(max_length=100, widget=forms.EmailInput (
        attrs={'class':'email'}))
        
    mdp_windows= forms.CharField(max_length=50, widget=forms.TextInput (
        attrs={'class':'mdp'}),required=False)
        
    probleme= forms.CharField(widget=forms.Textarea (
        attrs={'class':'probleme big-field-style', 'rows':'8', 'cols':'100'}))
        
    ref_commande= forms.CharField(max_length=50, widget=forms.TextInput (
        attrs={'class':'ref_commande'}))
        
    carton= forms.BooleanField (widget = forms.CheckboxInput (
        attrs={'class':'carton'}),required=False)
        
    alimentation=  forms.BooleanField (widget = forms.CheckboxInput (
        attrs={'class':'alimentation'}),required=False)
        
    reinitialisation=  forms.BooleanField (widget = forms.CheckboxInput (
        attrs={'class':'reinitialisation' }),required=False)
        

class client_form(forms.ModelForm):
    class Meta:
         model = depot
         fields = ["name","first_name","telephone","email","probleme","ref_commande"]
    name= forms.CharField(max_length=50, widget=forms.TextInput (
            attrs={'class':'nom'}))
            
    first_name= forms.CharField(max_length=50, widget=forms.TextInput (
            attrs={'class':'prenom'}))
            
    telephone= forms.CharField(max_length=50, widget=forms.TextInput (
            attrs={'class':'telephone'}))
            
    email= forms.EmailField(max_length=100, widget=forms.EmailInput (
            attrs={'class':'email'}))
    probleme= forms.CharField(max_length=500, widget=forms.Textarea (
            attrs={'class':'probleme', 'rows':'8'}))
            
    ref_commande= forms.CharField(max_length=50, widget=forms.TextInput (
            attrs={'class':'ref_commande'}))
    
    mdp_windows= forms.CharField(max_length=50, widget=forms.TextInput (
        attrs={'class':'mdp'}),required=False)
    

class form_modif_tech(forms.ModelForm):  
    class Meta:
         model = depot
         fields = ["commentaire","piece_a_modifier","statut","mdp_windows"]
    commentaire= forms.CharField(max_length=50, widget=forms.TextInput (
            attrs={'class':'commentaire'}))
            
    piece_a_modifier= forms.CharField(max_length=50, widget=forms.TextInput (
            attrs={'class':'piece_a_modifier'}))
            
    statut= forms.CharField(max_length=50, widget=forms.TextInput (
            attrs={'class':'statut'}))
            
    mdp_windows= forms.CharField(max_length=100, widget=forms.EmailInput (
            attrs={'class':'mdp_windows'}))
    
    raison_retour= forms.ChoiceField(choices=raison_retour_choix, widget=forms.Select (
        attrs={}))

class user_form(forms.ModelForm):
    class Meta:
        # password = forms.CharField(widget=forms.PasswordInput())
        model = CustomUser
        fields = ['first_name','last_name','password','poste']
        widgets = {
            # telling Django your password field in the mode is a password input on the template
            'password': forms.PasswordInput() 
        }

        

class afficher_client_form(forms.Form):
    ref_commande = forms.CharField(max_length=100,required=False)
    name = forms.CharField(max_length=100,required=False)
    first_name = forms.CharField(max_length=100,required=False)
    telephone = forms.CharField(max_length=100, required=False)
    email = forms.CharField(max_length=100, required=False)
    numero_depot = forms.CharField(max_length=100, required=False)






