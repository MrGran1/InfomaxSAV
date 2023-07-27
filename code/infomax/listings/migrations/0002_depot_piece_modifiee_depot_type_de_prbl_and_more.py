# Generated by Django 4.1 on 2023-07-27 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='depot',
            name='piece_modifiee',
            field=models.CharField(blank=True, default=None, max_length=1000),
        ),
        migrations.AddField(
            model_name='depot',
            name='type_de_prbl',
            field=models.CharField(blank=True, default=None, max_length=1000),
        ),
        migrations.AlterField(
            model_name='depot',
            name='mail_envoyee',
            field=models.CharField(choices=[('RC', 'Receptionné'), ('TR', 'En traitement'), ('TM', 'Terminé')], default='RC', max_length=100),
        ),
        migrations.AlterField(
            model_name='depot',
            name='numero_depot',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='depot',
            name='statut',
            field=models.CharField(choices=[('RC', 'Receptionné'), ('TR', 'En traitement'), ('TM', 'Terminé')], default='RC', max_length=100),
        ),
    ]
