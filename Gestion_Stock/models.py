from django.db import models

#login model
class Comptes(models.Model):
    username=models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=20)



#typeproduit
class type_produit(models.Model):
    designation=models.CharField(max_length=50)



#produit
class produit(models.Model):
    designation=models.CharField(max_length=50)
    type=models.ForeignKey(type_produit,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.Description_cmd)
    


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