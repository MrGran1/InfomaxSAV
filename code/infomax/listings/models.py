from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.

class client(models.Model):
    name = models.fields.CharField(max_length=50)
    fist_name = models.fields.CharField(max_length=50)
    telephone = models.fields.IntegerField(max_length=50)
    email = models.fields.CharField(max_length=100)
    
class ordinateur(models.Model):
    mdp_windows = models.fields.CharField(max_length=50)
    probleme = models.fields.CharField(max_length=500)
    carton = models.fields.BooleanField(default=False)
    alimentation = models.fields.BooleanField(default=False)
    piece_a_modifier = models.fields.CharField(max_length=100,null=True)
    reinitialisation = models.fields.BooleanField(default=False)
    proprietaire = models.ForeignKey(client, null = False, on_delete=models.CASCADE)

class depot(models.Model):
    ref_depot = models.fields.CharField(max_length=50)
    total_a_payer = models.fields.IntegerField()
    numero_depot = models.fields.IntegerField(primary_key=True, default=1000)
    commentaire = models.fields.CharField(default = '' ,max_length=1000)
    date = models.fields.DateField(validators = [MinValueValidator(2020)],default=2020)
    ordinateur = models.ForeignKey(ordinateur,null = True, on_delete=models.CASCADE)
#    vendeur = models.ForeignKey(vendeur,null = True, on_delete=models.CASCADE)

class vendeur(models.Model): #Technicien et vendeur
    class type_vendeur(models.TextChoices):
        Technicien = 'TC'
        Commerciale = 'CO'

    name = models.fields.CharField(max_length=50)
    fist_name = models.fields.CharField(max_length=50)
    type = models.fields.CharField(choices=type_vendeur.choices,max_length=5)
    id = models.fields.IntegerField(primary_key=True,default=1000)
