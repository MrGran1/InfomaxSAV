# Generated by Django 4.1 on 2023-07-26 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depot',
            name='mail_envoyee',
            field=models.CharField(choices=[('RC', 'Receptionné'), ('TR', 'En traitement'), ('TM', 'Terminé')], default='RC', max_length=100),
        ),
        migrations.AlterField(
            model_name='depot',
            name='statut',
            field=models.CharField(choices=[('RC', 'Receptionné'), ('TR', 'En traitement'), ('TM', 'Terminé')], default='RC', max_length=100),
        ),
    ]