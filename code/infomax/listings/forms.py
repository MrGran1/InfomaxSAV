from django import forms
from listings.models import depot,CustomUser
from .models import depot

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
        
    probleme= forms.CharField(max_length=500, widget=forms.Textarea (
        attrs={'class':'probleme', 'rows':'8'}))
        
    ref_commande= forms.CharField(max_length=50, widget=forms.TextInput (
        attrs={'class':'ref_commande'}))
        
    carton= forms.BooleanField (widget = forms.CheckboxInput (
        attrs={'class':'carton'}),required=False)
        
    alimentation=  forms.BooleanField (widget = forms.CheckboxInput (
        attrs={'class':'alimentation'}),required=False)
        
    reinitialisation=  forms.BooleanField (widget = forms.CheckboxInput (
        attrs={'class':'reinitialisation' }),required=False)
        



class client_form(forms.ModelForm):
        
    nom= forms.CharField(max_length=50, widget=forms.TextInput (
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

    class form_modif_tech(forms.ModelForm):
    
        class Meta(forms.ModelForm):
            model = depot
            fields = ('commentaire','piece_a_modifier','statut','mdp_windows')    

class user_form(forms.ModelForm):
    class Meta:
        # password = forms.CharField(widget=forms.PasswordInput())
        model = CustomUser
        fields = ['first_name','last_name','password','is_superuser','poste']
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






