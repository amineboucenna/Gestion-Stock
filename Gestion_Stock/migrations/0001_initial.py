# Generated by Django 4.1.4 on 2023-01-29 11:06

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='achat_entree_stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qte', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10000)])),
                ('prix_achat', models.FloatField(default=0, max_length=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('prix_vente', models.FloatField(default=0, max_length=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('tot', models.FloatField(default=0, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='bl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_document', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='bon_commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_document', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('qte', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10000)])),
            ],
        ),
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('prenom', models.CharField(max_length=20)),
                ('adress', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=10)),
                ('credits_client', models.FloatField(default=0, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Comptes',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='fournisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('prenom', models.CharField(max_length=20)),
                ('adress', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=10)),
                ('solde', models.FloatField(default=0, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='sortie_stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qte_a_enlever', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10000)])),
                ('motif', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_saisie', models.DateTimeField(default=datetime.datetime.now)),
                ('qte', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10000)])),
                ('prix_achat', models.FloatField(default=0, max_length=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('prix_vente', models.FloatField(default=0, max_length=10, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='type_produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='vente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qte_a_vendre', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10000)])),
                ('code_client', models.ManyToManyField(related_name='code_client_vente', to='Gestion_Stock.client')),
                ('produit_a_vendre', models.ManyToManyField(related_name=',code_produit_vente+', to='Gestion_Stock.stock')),
            ],
        ),
        migrations.CreateModel(
            name='reglement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_reglemet', models.DateTimeField(default=datetime.datetime.now)),
                ('nom_fournisseur', models.CharField(max_length=20)),
                ('prix_reglement_facture', models.FloatField(default=0, max_length=10)),
                ('prix_reglement_bl', models.FloatField(default=0, max_length=10)),
                ('code_bon_livraison', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion_Stock.bl')),
            ],
        ),
        migrations.CreateModel(
            name='produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=50)),
                ('type_produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type_produit', to='Gestion_Stock.type_produit')),
            ],
        ),
        migrations.CreateModel(
            name='facture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_document', models.DateTimeField(default=datetime.datetime.now)),
                ('code_document', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='code_document1', to='Gestion_Stock.bon_commande')),
                ('facture_avoir', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fournisseur_facture', to='Gestion_Stock.fournisseur')),
            ],
        ),
        migrations.AddField(
            model_name='bon_commande',
            name='contient',
            field=models.ManyToManyField(related_name='produit', to='Gestion_Stock.produit'),
        ),
        migrations.AddField(
            model_name='bl',
            name='bl_avoir',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fornisseur_bl', to='Gestion_Stock.fournisseur'),
        ),
        migrations.AddField(
            model_name='bl',
            name='code_document',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='code_document2', to='Gestion_Stock.bon_commande'),
        ),
    ]
