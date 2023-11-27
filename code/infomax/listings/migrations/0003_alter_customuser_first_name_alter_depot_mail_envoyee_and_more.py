# Generated by Django 4.2.5 on 2023-11-27 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_depot_first_name_tech_depot_last_name_tech'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='depot',
            name='mail_envoyee',
            field=models.CharField(choices=[('', '---------'), ('AT', 'A traiter'), ('RC', 'Retour SAV constructeur'), ('AR', 'Attente retour client'), ('AP', 'Attente réapprovisionnement produits'), ('Fait', 'Fait'), ('TM', 'Recupéré par le client')], default='AT', max_length=100),
        ),
        migrations.AlterField(
            model_name='depot',
            name='statut',
            field=models.CharField(choices=[('', '---------'), ('AT', 'A traiter'), ('RC', 'Retour SAV constructeur'), ('AR', 'Attente retour client'), ('AP', 'Attente réapprovisionnement produits'), ('Fait', 'Fait'), ('TM', 'Recupéré par le client')], default='AT', max_length=100),
        ),
    ]
