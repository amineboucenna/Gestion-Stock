from datetime import datetime
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

#login model
class Comptes(models.Model):
    username=models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=20)



#typeproduit
class type_produit(models.Model):
    designation=models.CharField(max_length=50)
    def __str__(self):
        return self.designation 
    



#produit
class produit(models.Model):
    designation=models.CharField(max_length=50)
    type=models.CharField(max_length=50)
    typep=models.ForeignKey(type_produit,on_delete=models.CASCADE,related_name='type_produit')
    qte = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(10000)])
    prix_achat=models.FloatField(max_length=10,default=0,validators=[MinValueValidator(0)])
    prix_vente=models.FloatField(max_length=10,default=0,validators=[MinValueValidator(0)])
    def __str__(self):
        return self.typep.designation
    def __str__(self):
        return self.designation
    


#client
class client(models.Model):
    nom=models.CharField(max_length=20)
    prenom=models.CharField(max_length=20)
    adress=models.CharField(max_length=50)
    telephone=models.CharField(max_length=10)


#fournisseur
class fournisseur(models.Model):
    nom=models.CharField(max_length=20)
    prenom=models.CharField(max_length=20)
    adress=models.CharField(max_length=50)
    telephone=models.CharField(max_length=10)
    solde=models.FloatField(max_length=10,default=0)
    def __str__(self):
        return self.nom+' '+self.prenom


#bon de commande
class bon_commande(models.Model):
    code_document = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    qte = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10000)])
    contient = models.ManyToManyField(produit,related_name='produit')
    def __str__(self):
        return  self.contient.designation
    def __str__(self):
        return  self.contient.typep.designation
    def __str__(self):
        return self.code_document.__str__()

#facture
class facture(models.Model):
    code_document = models.OneToOneField(bon_commande,on_delete=models.CASCADE,related_name='code_document1')
    date_document = models.DateTimeField(default=datetime.now)
    facture_avoir = models.ForeignKey(fournisseur,on_delete=models.CASCADE,related_name='fournisseur_facture')
    

#BL
class bl(models.Model):
    code_document = models.OneToOneField(bon_commande,on_delete=models.CASCADE,related_name='code_document2')
    date_document = models.DateTimeField(default=datetime.now)
    bl_avoir = models.ForeignKey(fournisseur,on_delete=models.CASCADE,related_name='fornisseur_bl')


#entree stock
class entree_stock(models.Model):
    contient_produit=models.ManyToManyField(bon_commande)
    def __str__(self):
        return self.contient_produit.contient
