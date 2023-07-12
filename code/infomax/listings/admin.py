from django.contrib import admin
from django.contrib.auth.models import AbstractUser

# Register your models here.

from listings.models import *

admin.site.register(depot)