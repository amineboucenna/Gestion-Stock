from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

#typeproduit
class type_produit(models.Model):
    designation=models.CharField(max_length=50)



#produit
class produit(models.Model):
    designation=models.CharField(max_length=50)
    type=models.ForeignKey(type_produit)
    


#client
class client(models.Model):
    nom=models.CharField(max_length=20)
    prenom=models.CharField(max_length=20)
    adress=models.CharField(max_length=50)
    telephone=PhoneNumberField()
    achete=models.ManyToManyField(produit)


#fournisseur
class fournisseur(models.Model):
    nom=models.CharField(max_length=20)
    prenom=models.CharField(max_length=20)
    adress=models.CharField(max_length=50)
    telephone=PhoneNumberField()
    fournir=models.ManyToOneRel(field=produit.pk,to=produit)

class Comptes(models.Model):
    username=models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=20)