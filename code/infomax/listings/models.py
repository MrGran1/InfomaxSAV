from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractUser
# Create your models here.

class depot(models.Model):

    statut_choix = [
        ("RC", "Receptionné"),
        ("TR", "En traitement"),
        ("TR", "Terminé")
    ]
#Relatif au client
    name = models.fields.CharField(max_length=50,null = True)
    first_name = models.fields.CharField(max_length=50,null = True)
    telephone = models.fields.CharField(max_length=50,null = True)
    email = models.fields.CharField(max_length=100,null = True)
    
### Relatif à l'ordi
    mdp_windows = models.fields.CharField(max_length=50,blank = True, default = None)
    probleme = models.fields.CharField(max_length=500,blank = True,default = None)
    carton = models.fields.BooleanField(default=False)
    alimentation = models.fields.BooleanField(default=False)
    piece_a_modifier = models.fields.CharField(max_length=100,blank = True,default = None)
    reinitialisation = models.fields.BooleanField(default=False)

## Relatif au dépot

    ref_depot = models.fields.CharField(max_length=50)
    total_a_payer = models.fields.IntegerField(validators = [MinValueValidator(0)],default = 0)
    numero_depot = models.fields.IntegerField(primary_key=True,validators = [MinValueValidator(2000)])
    commentaire = models.fields.CharField(default = None,blank = True ,max_length=1000,)
    date = models.fields.DateField(default=2020)
    statut = models.fields.CharField(choices = statut_choix ,max_length=100,null = False ,default = "RC")
    mail_envoyee = models.fields.CharField(choices = statut_choix ,max_length=100,null = False ,default = "RC")
 
 ### Vendeur #########
    first_name_seller =  models.fields.CharField(max_length=50)
    last_name_seller =  models.fields.CharField(max_length=50)





class CustomUser(AbstractUser):
    type_vendeur = [

        ("TC" , 'Technicien'),
        ("CO" , 'Commerciale')
    ]

    poste = models.fields.CharField(choices = type_vendeur ,max_length=100,null = False ,default = "CO")