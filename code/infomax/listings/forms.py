from django import forms
from listings.models import client

class client_form(forms.ModelForm):
    class Meta :
        model = client
        fields = '__all__'

#     name_client = forms.CharField(max_length=50)
#     fist_name = forms.CharField(max_length=50)
#     telephone = forms.CharField(max_length=50)
#     email = forms.CharField(max_length=100)


# class creation_
#     mdp_windows = forms.CharField(max_length=50)
#     probleme = forms.CharField(max_length=500)
#     carton = forms.BooleanField(default=False)
#     alimentation = forms.BooleanField(default=False)
#     piece_a_modifier = forms.CharField(max_length=100,null=True)
#     reinitialisation = forms.BooleanField(default=False)

#     ref_depot = forms.CharField(max_length=50)
#     total_a_payer = forms.IntegerField()
#     numero_depot = forms.IntegerField(primary_key=True, default=1000)
#     commentaire = forms.CharField(default = '' ,max_length=1000)
