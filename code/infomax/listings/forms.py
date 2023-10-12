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
        attrs={'class':'mode_envoi''form-field', 'style':'width : 100% ; height : 40px;'}))
        
    designation= forms.ChoiceField(choices=designation_choix, widget=forms.Select(
        attrs={'class':'designation''form-field', 'style':'width : 100% ; height : 40px;'}))
        
    nom= forms.CharField(max_length=50, widget=forms.TextInput (
        attrs={'class':'nom''form-field', 'style':'width : 100% ; height : 40px;'}))
        
    first_name= forms.CharField(max_length=50, widget=forms.TextInput (
        attrs={'class':'prenom''form-field', 'style':'width : 100% ; height : 40px;'}))
        
    telephone= forms.CharField(max_length=50, widget=forms.TextInput (
        attrs={'class':'telephone''form-field', 'style':'width : 100% ; height : 40px;'}))
        
    email= forms.EmailField(max_length=100, widget=forms.TextInput (
        attrs={'class':'email''form-field', 'style':'width : 100% ; height : 40px;'}))
        
    mdp_windows= forms.CharField(max_length=50, widget=forms.TextInput (
        attrs={'class':'mdp''form-field', 'style':'width : 100% ; height : 40px;'}))
        
    probleme= forms.CharField(max_length=500, widget=forms.Textarea (
        attrs={'class':'probleme''form-field', 'rows':'4'}))
        
    ref_commande= forms.CharField(max_length=50, widget=forms.TextInput (
        attrs={'class':'ref_commande''form-field', 'style':'width : 100% ; height : 40px;'}))
        
    carton= forms.BooleanField (widget = forms.CheckboxInput (
        attrs={'class':'carton' 'form-field'}))
        
    alimentation=  forms.BooleanField (widget = forms.CheckboxInput (
        attrs={'class':'alimentation' 'form-field'}))
        
    reinitialisation=  forms.BooleanField (widget = forms.CheckboxInput (
        attrs={'class':'reinitialisation' 'form-field'}))
        



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
    ref_commande = forms.CharField(max_length=100,required=False)
    name = forms.CharField(max_length=100,required=False)
    first_name = forms.CharField(max_length=100,required=False)
    telephone = forms.CharField(max_length=100, required=False)
    email = forms.CharField(max_length=100, required=False)
    numero_depot = forms.CharField(max_length=100, required=False)






