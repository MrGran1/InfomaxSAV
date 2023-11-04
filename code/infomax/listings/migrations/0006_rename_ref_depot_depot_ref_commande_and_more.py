# Generated by Django 4.2.5 on 2023-10-19 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_alter_depot_commentaire_alter_depot_designation_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='depot',
            old_name='ref_depot',
            new_name='ref_commande',
        ),
        migrations.AlterField(
            model_name='depot',
            name='alimentation',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='depot',
            name='carton',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='depot',
            name='mdp_windows',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='depot',
            name='piece_a_modifier',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='depot',
            name='reinitialisation',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
