from django.db.models import fields
from django import forms
from .models import bl, bon_commande, facture, produit,client,fournisseur, type_produit
class Creer_produit(forms.ModelForm):
    class Meta:
        model = produit
        fields="__all__"

class Creer_typep(forms.ModelForm):
    class Meta:
        model = type_produit
        fields="__all__"


class Creer_client(forms.ModelForm):
    class Meta:
        model = client
        fields="__all__"



class Creer_fournisseur(forms.ModelForm):
    class Meta:
        model = fournisseur
        fields="__all__"


class Creer_bon_commande(forms.ModelForm):
    class Meta:
        model = bon_commande
        fields= 'code_document' , 'contient' , 'qte',



class Creer_facture(forms.ModelForm):
    class Meta:
        model = facture
        fields="__all__"


class Creer_bl(forms.ModelForm):
    class Meta:
        model = bl
        fields="__all__"