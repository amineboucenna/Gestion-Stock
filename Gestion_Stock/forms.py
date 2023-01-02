from django.db.models import fields
from django import forms
from .models import produit,client,fournisseur
class Creer_produit(forms.ModelForm):
    class Meta:
        model = produit
        fields="__all__"


class Creer_client(forms.ModelForm):
    class Meta:
        model = client
        fields="__all__"



class Creer_fournisseur(forms.ModelForm):
    class Meta:
        model = fournisseur
        fields="__all__"