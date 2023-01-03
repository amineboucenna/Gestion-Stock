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
    def __getname__(self):
        return self.designation 
    



#produit
class produit(models.Model):
    designation=models.CharField(max_length=50)
    type=models.CharField(max_length=50)
    typep=models.ForeignKey(type_produit,on_delete=models.CASCADE,related_name='type_produit')
    def __str__(self):
        return str(self)
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


#bon de commande
class bon_commande(models.Model):
    code_document = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    qte = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10000)])
    contient = models.ManyToManyField(produit,related_name='produit')


#facture
class facture(models.Model):
    code_document = models.OneToOneField(bon_commande,on_delete=models.CASCADE,related_name='asdssd')
    date_document = models.DateTimeField(default=datetime.now)
    facture_etablie_bonc = models.OneToOneField(bon_commande,on_delete=models.CASCADE,related_name='qsasaa')
    facture_avoir = models.ForeignKey(fournisseur,on_delete=models.CASCADE,related_name='adsq')


#BL
class bl(models.Model):
    code_document = models.OneToOneField(bon_commande,on_delete=models.CASCADE,related_name='lol')
    date_document = models.DateTimeField(default=datetime.now)
    bl_etablie_bonc = models.OneToOneField(bon_commande,on_delete=models.CASCADE,related_name='hello')
    bl_avoir = models.ForeignKey(fournisseur,on_delete=models.CASCADE,related_name='dsssdsa')
    def __str__(self):
        return (self.Creer_bl)