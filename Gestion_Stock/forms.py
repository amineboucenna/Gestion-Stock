from django.db.models import fields
from django import forms
from .models import bl, bon_commande, facture, produit,client,fournisseur, type_produit,achat_entree_stock,sortie_stock,vente
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
        fields="__all__"



class Creer_facture(forms.ModelForm):
    class Meta:
        model = facture
        fields="__all__"


class Creer_bl(forms.ModelForm):
    class Meta:
        model = bl
        fields="__all__"


class Creer_entree_S(forms.ModelForm):
    class Meta:
        model = achat_entree_stock
        fields ="__all__"



class Creer_sortie_S(forms.ModelForm):
    class Meta:
        model = sortie_stock
        fields ="__all__"
        

class Creer_vente(forms.ModelForm):
    class Meta : 
        model = vente
        fields ="__all__"