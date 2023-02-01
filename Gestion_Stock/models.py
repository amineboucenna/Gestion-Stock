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
    type_produit=models.ForeignKey(type_produit,on_delete=models.CASCADE,related_name='type_produit')
    def __str__(self):
        return self.type_produit.designation
    def __str__(self):
        return self.designation
    


#client
class client(models.Model):
    nom=models.CharField(max_length=20)
    prenom=models.CharField(max_length=20)
    adress=models.CharField(max_length=50)
    telephone=models.CharField(max_length=10)
    credits_client=models.FloatField(max_length=10,default=0)
    def __str__(self):
        return self.nom+' '+self.prenom



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
        return self.code_document.__str__()
    def get_bon(self):
        return self.bon_commande.all()

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


#reglement
class reglement(models.Model):
    code_bon_livraison=models.ForeignKey(bl,on_delete=models.CASCADE)
    date_reglemet=models.DateTimeField(default=datetime.now)
    nom_fournisseur=models.CharField(max_length=20)
    prix_reglement_facture=models.FloatField(max_length=10,default=0)
    prix_reglement_bl=models.FloatField(max_length=10,default=0)

#entree stock
class achat_entree_stock(models.Model):
    id_commande=models.ManyToOneRel(to=bon_commande,field=bon_commande.code_document,field_name=bon_commande.code_document,on_delete=models.CASCADE,related_name='bon_commande')
    id_produit=models.ManyToOneRel(to=produit,on_delete=models.CASCADE,field=produit.pk,field_name=produit.pk)
    qte = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(10000)])
    prix_achat=models.FloatField(max_length=10,default=0,validators=[MinValueValidator(0)])
    prix_vente=models.FloatField(max_length=10,default=0,validators=[MinValueValidator(0)])
    tot=models.FloatField(max_length=10,default=0)
    def __str__(self):
        return self.achat_entree_stock.all()
    

###################
#STOCK

class stock(models.Model):
    id_produit=models.ManyToOneRel(to=produit,on_delete=models.CASCADE,field=produit.pk,field_name=produit.pk)
    date_saisie=models.DateTimeField(default=datetime.now)
    qte = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(10000)])
    prix_achat=models.FloatField(max_length=10,default=0,validators=[MinValueValidator(0)])
    prix_vente=models.FloatField(max_length=10,default=0,validators=[MinValueValidator(0)])


    

class sortie_stock(models.Model):
    id_produit=models.ManyToOneRel(to=produit,on_delete=models.CASCADE,field=produit.pk,field_name=produit.pk)
    qte_a_enlever=models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(10000)])
    motif=models.CharField(max_length=50)


#VENTE
class vente(models.Model):
    code_client=models.ManyToManyField(to=client,related_name='code_client_vente')
    produit_a_vendre=models.ManyToManyField(to=stock,related_name=',code_produit_vente+')
    qte_a_vendre=models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(10000)])