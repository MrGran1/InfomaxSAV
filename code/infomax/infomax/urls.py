"""infomax URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from listings import views
from django.contrib.auth import views as auth_views
from listings.views import login_view 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', views.create_client,name ='creation_bon_depot'),
    path('login/', login_view,name='login'),
    path('logout/' , views.logout_view,name = 'logout'),
    path('create_user/', views.create_user,name = "creation_user" ),
    path('home/', views.home ),
    path('afficher/', views.afficher_client, name = 'afficher'),
    path('depot_com/<int:id>', views.modif_depot, name = 'depot_modif_com'),
    path('depot_tech/<int:id>', views.depot_tech, name = 'depot_modif_tec'),
    path('pdf/<int:id>', views.create_pdf),
    path('afficher_users/', views.afficher_user),
    path('supprimer_user/<str:username>', views.supprimer_user, name = 'supprimer_user')
]
