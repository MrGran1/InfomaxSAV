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


choix = [
        ('', '---------'),
        ('PO', 'Laptop'),
        ('CO', 'Config'),
        ('AR', 'Article')
        
    ]
class form_input(forms.Form):
    designation_choix= forms.MultipleChoiceField(choices=choix, widget=forms.SelectMultiple(attrs={'class':'custom-select'}))


class client_form(forms.ModelForm):
    
    class Meta(forms.ModelForm):
        model = depot
        exclude = ('numero_depot','first_name_seller','last_name_seller','date','mail_envoyee','commentaire','piece_a_modifier','statut')
        nom= forms.CharField(
            label='Nom',
            widget=form_input()
        )
        

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






