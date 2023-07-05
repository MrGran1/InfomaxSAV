from django import forms
from listings.models import depot,CustomUser

class client_form(forms.ModelForm):
    class Meta :
        model = depot
        exclude = ('numero_depot','first_name_seller','last_name_seller','date','statut')


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
    ref_depot = forms.CharField(max_length=100)
