from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractUser
# Create your models here.

class depot(models.Model):

    statut_choix = [
        ('', '---------'),
        ("RC", "Receptionné"),
        ("TR", "En traitement"),
        ("TM", "Terminé")
    ]

    envoi_choix = [
        ('', '---------'),
        ('RE', 'Retrait'),
        ('EX', 'Expédition')
        
    ]

    designation_choix = [
        ('', '---------'),
        ('PO', 'Laptop'),
        ('CO', 'Config'),
        ('AR', 'Article')
        
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

    ### portable, article, config
    ### retrait expema
#Relatif au client
    ref_commande = models.fields.CharField(max_length=50)
    name = models.fields.CharField(max_length=50,null = True)
    first_name = models.fields.CharField(max_length=50,null = True)
    telephone = models.fields.CharField(max_length=50,null = True)
    email = models.fields.CharField(max_length=100,null = True)
    
### Relatif à l'ordi
    mdp_windows = models.fields.CharField(max_length=50,blank = True, null = True, default = None)
    probleme = models.fields.TextField(max_length=500,blank = True,default = None)
    carton = models.fields.BooleanField(default=False,blank =True)
    alimentation = models.fields.BooleanField(default=False,blank=True)
    reinitialisation = models.fields.BooleanField(default=False,blank=True)
    piece_a_modifier = models.fields.CharField(max_length=100,null = True,default = "")

## Relatif au dépot

   
    total_a_payer = models.fields.IntegerField(validators = [MinValueValidator(0)],default = 0)
    numero_depot = models.fields.AutoField(primary_key=True)
    date = models.fields.DateField(default=2020)
    statut = models.fields.CharField(choices = statut_choix ,max_length=100,null = False ,default = "RC")
    mail_envoyee = models.fields.CharField(choices = statut_choix ,max_length=100,null = False ,default = "RC")
    commentaire = models.fields.CharField(default = "",blank = True ,max_length=1000)

    designation = models.fields.CharField(choices = designation_choix ,max_length=100,null = False ,default = '')
    mode_envoi = models.fields.CharField(choices = envoi_choix ,max_length=100,null = False ,default = "")
    raison_retour = models.fields.CharField(choices = raison_retour_choix ,max_length=100,null = False ,default = "")

 ### Vendeur #########
    first_name_seller =  models.fields.CharField(max_length=50)
    last_name_seller =  models.fields.CharField(max_length=50)
    
### Technicien ####
    first_name_tech =  models.fields.CharField(max_length=50,blank=True)
    last_name_tech =  models.fields.CharField(max_length=50,blank=True)



class CustomUser(AbstractUser):
    type_vendeur = [

        ("TC" , 'Technicien'),
        ("CO" , 'Commerciale')
    ]

    poste = models.fields.CharField(choices = type_vendeur ,max_length=100,null = False ,default = "CO")




