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
    mode_envoi= forms.MultipleChoiceField(choices=envoi_choix, widget=forms.SelectMultiple(attrs={'class':'mode_envoi'}))
    designation= forms.MultipleChoiceField(choices=designation_choix, widget=forms.SelectMultiple(attrs={'class':'designation'}))
    nom= forms.CharField(max_length=50, widget=forms.TextInput (attrs={'class':'nom''form-field'}))
    first_name= forms.CharField(max_length=50, widget=forms.TextInput (attrs={'class':'prenom'}))
    telephone= forms.CharField(max_length=50, widget=forms.TextInput (attrs={'class':'telephone'}))
    email= forms.EmailField(max_length=100, widget=forms.TextInput (attrs={'class':'email'}))
    mdp_windows= forms.CharField(max_length=50, widget=forms.TextInput (attrs={'class':'mdp'}))
    probleme= forms.CharField(max_length=500, widget=forms.TextInput (attrs={'class':'probleme'}))
    ref_commande= forms.CharField(max_length=50, widget=forms.TextInput (attrs={'class':'nomref_commande'}))



class client_form(forms.ModelForm):
    
    class Meta(forms.ModelForm):
        model = depot
        exclude = ('numero_depot','first_name_seller','last_name_seller','date','mail_envoyee','commentaire','piece_a_modifier','statut')


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
    ref_commande = forms.CharField(max_length=100,required=True)
    name = forms.CharField(max_length=100,required=True)
    first_name = forms.CharField(max_length=100,required=True)
    telephone = forms.CharField(max_length=100, required=True)
    email = forms.CharField(max_length=100, required=True)
    numero_depot = forms.CharField(max_length=100, required=True)






