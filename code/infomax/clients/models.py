from django.db import models

# Create your models here.
class clients (models.Model):
    name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)