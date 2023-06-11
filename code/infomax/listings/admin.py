from django.contrib import admin

# Register your models here.

from listings.models import *

admin.site.register(ordinateur)
admin.site.register(client)
admin.site.register(depot)