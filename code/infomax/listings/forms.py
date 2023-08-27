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
    mode_envoi= forms.MultipleChoiceField(choices=envoi_choix, widget=forms.SelectMultiple(attrs={'class':'custom-select'}))
    designation= forms.MultipleChoiceField(choices=designation_choix, widget=forms.SelectMultiple(attrs={'class':'custom-select'}))
    name= forms.CharField(max_length=50)
    first_name= forms.CharField(max_length=50)
    telephone= forms.CharField(max_length=50)
    email= forms.EmailField(max_length=50)
    mdp_windows= forms.CharField(max_length=50)
    probleme= forms.CharField(max_length=500)
    ref_commande= forms.CharField(max_length=50)



class client_form(forms.ModelForm):
    
    class Meta(forms.ModelForm):
        model = depot
        exclude = ('numero_depot','first_name_seller','last_name_seller','date','mail_envoyee','commentaire','piece_a_modifier','statut')

        

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
    ref_depot = forms.CharField(max_length=100,required=False)
    name = forms.CharField(max_length=100,required=False)
    first_name = forms.CharField(max_length=100,required=False)






