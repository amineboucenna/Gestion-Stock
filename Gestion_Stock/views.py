#imports for generating pdf file

import datetime
import io
from reportlab.pdfgen import canvas

from django.http import FileResponse
from django.shortcuts import redirect, render

#imports for views

from .forms import (Creer_bl, Creer_bon_commande, Creer_client, Creer_facture,
                    Creer_fournisseur, Creer_produit, Creer_typep)
from .models import (Comptes, bl, bon_commande, client, facture, fournisseur,
                     produit, type_produit)



# Create your views here.

def redirect_login(request):
    return redirect('loginpage')

def Verify_Login(request):
    if request.method == "GET" : 
        accountquery=request.GET.get('usernameinput')      
        if accountquery :
            database_username=Comptes.objects.filter(username = accountquery )   
            passwordquery=request.GET.get('passwordinput')
            if database_username :
                if database_username[0].username == accountquery and database_username[0].password == passwordquery :
                    return redirect('produits')
                else :
                    msg = 'Incorrect username or password'
                    return render(request,"login.html",{"msg":msg})
            else :
                msg = 'The user given does not exist'
                return render(request,"login.html",{"msg":msg})
        else :
            return render(request,"login.html")



def Logout(request):
    return render(request,"login.html")


###############################################################################################
# les views de type_produit :

def modifier_type_produit(request,pk):
    try : 
        typep=type_produit.objects.get(id=pk)
    except : 
        return redirect('produits')
    if request.method == 'POST' :
        form = Creer_typep(request.POST,instance=typep)
        if form.is_valid() : 
            form.save()
            return redirect('produits')

    else :
        form=Creer_typep(instance=typep)
        return render(request,'operations/produit/modifiertypep.html',{"form":form})



def supprimer_type_produit(request,pk):
    typep=''
    if request.method == 'POST' :
        typep=type_produit.objects.get(id=pk)
        typep.delete()
        return redirect('produits')
    else :
        typep=type_produit.objects.get(id=pk)
        return render(request,'operations/produit/supprimertypep.html',{"prod":typep})




###############################################################################################
################# GESTION #########################################
# les views de produit : 
def lister_produit(request):
    if request.method == 'POST' :
        form=Creer_produit(request.POST)
        if form.is_valid() :
            form.save()
            form=Creer_produit()
            form_typep=Creer_typep()
            prod = produit.objects.all()
            typep = type_produit.objects.all()
            return render(request,"operations/produit/liste.html",{"typep":typep,"prod":prod,"form_typep":form_typep,"form":form})
        form=Creer_typep(request.POST)
        if form.is_valid() :
            form.save()
            form=Creer_produit()
            form_typep=Creer_typep()
            prod = produit.objects.all()
            typep = type_produit.objects.all()
            return render(request,"operations/produit/liste.html",{"typep":typep,"prod":prod,"form_typep":form_typep,"form":form})
    else:
        form=Creer_produit()
        form_typep=Creer_typep()
        prod = produit.objects.all()
        typep = type_produit.objects.all()
        return render(request,"operations/produit/liste.html",{"typep":typep,"prod":prod,"form_typep":form_typep,"form":form})


def modifier_produit(request,pk):
    try : 
        cmd=produit.objects.get(id=pk)
    except : 
        return redirect('produits')
    if request.method == 'POST' :
        form = Creer_produit(request.POST,instance=cmd)
        if form.is_valid() : 
            form.save()
            return redirect('produits')

    else :
        form=Creer_produit(instance=cmd)
        return render(request,'operations/produit/modifier.html',{"form":form})



def supprimer_produit(request,pk):
    prod=''
    if request.method == 'POST' :
        prod=produit.objects.get(id=pk)
        prod.delete()
        return redirect('produits')
    else :
        prod=produit.objects.get(id=pk)
        return render(request,'operations/produit/supprimer.html',{"prod":prod})


def rechercher_produit(request):
    prod=''
    if request.method == "GET" :
        query=request.GET.get("rechercher")
        if query : 
            prod=produit.objects.filter(designation__contains=query)
        return render(request,"operations/produit/rechercher.html",{"prod":prod})
    else :
        return render(request,"operations/produit/rechercher.html")


def rechercher_type_produit(request):
    prod=''
    if request.method == "GET" :
        query=request.GET.get("rechercher")
        if query : 
            prod=produit.objects.filter(type__contains=query)
        return render(request,"operations/produit/rechercher.html",{"prod":prod})
    else :
        return render(request,"operations/produit/rechercher.html")


def rechercher_typep_produit(request):
    prod=''
    if request.method == "GET" :
        query=request.GET.get("rechercher")
        if query : 
            prod=produit.objects.filter(typep_designation__contains=query)
        return render(request,"operations/produit/rechercher.html",{"prod":prod})
    else :
        return render(request,"operations/produit/rechercher.html")



###############################################################################################
#les views de clients 
def lister_client(request):
    if request.method == 'POST' :
        form=Creer_client(request.POST)
        if form.is_valid() :
            form.save()
            form=Creer_client()
            clients = client.objects.all()
            return render(request,"operations/lesclients/liste.html",{"clients":clients,"form":form})
    else:
        form=Creer_client()
        clients = client.objects.all()
        return render(request,"operations/lesclients/liste.html",{"clients":clients,"form":form})


def modifier_client(request,pk):
    try : 
        clients=client.objects.get(id=pk)
    except : 
        return redirect('clients')
    if request.method == 'POST' :
        form = Creer_client(request.POST,instance=clients)
        if form.is_valid() : 
            form.save()
            return redirect('clients')

    else :
        form=Creer_client(instance=clients)
        return render(request,'operations/lesclients/modifier.html',{"form":form})



def supprimer_client(request,pk):
    clients=''
    if request.method == 'POST' :
        clients=client.objects.get(id=pk)
        clients.delete()
        return redirect('clients')
    else :
        clients=client.objects.get(id=pk)
        return render(request,'operations/lesclients/supprimer.html',{"c":clients})


def rechercher_client(request):
    clients=''
    if request.method == "GET" :
        query=request.GET.get("rechercher")
        if query : 
            clients=client.objects.filter(nom__contains=query)
        return render(request,"operations/lesclients/rechercher.html",{"clients":clients})
    else :
        return render(request,"operations/lesclients/rechercher.html")



###############################################################################################
#les views de fournisseur 
def lister_fournisseur(request):
    if request.method == 'POST' :
        form=Creer_fournisseur(request.POST)
        if form.is_valid() :
            form.save()
            form=Creer_fournisseur()
            fournisseurs = fournisseur.objects.all()
            return render(request,"operations/fournisseur/liste.html",{"fournisseurs":fournisseurs,"form":form})
    else:
        form=Creer_fournisseur()
        fournisseurs = fournisseur.objects.all()
        return render(request,"operations/fournisseur/liste.html",{"fournisseurs":fournisseurs,"form":form})


def modifier_fournisseur(request,pk):
    try : 
        fournisseurs=fournisseur.objects.get(id=pk)
    except : 
        return redirect('fournisseurs')
    if request.method == 'POST' :
        form = Creer_fournisseur(request.POST,instance=fournisseurs)
        if form.is_valid() : 
            form.save()
            return redirect('fournisseurs')

    else :
        form=Creer_fournisseur(instance=fournisseurs)
        return render(request,'operations/fournisseur/modifier.html',{"form":form})



def supprimer_fournisseur(request,pk):
    fournisseurs=''
    if request.method == 'POST' :
        fournisseurs=fournisseur.objects.get(id=pk)
        fournisseurs.delete()
        return redirect('fournisseurs')
    else :
        fournisseurs=fournisseur.objects.get(id=pk)
        return render(request,'operations/fournisseur/supprimer.html',{"f":fournisseurs})


def rechercher_fournisseur(request):
    fournisseurs=''
    if request.method == "GET" :
        query=request.GET.get("rechercher")
        if query : 
            fournisseurs=fournisseur.objects.filter(nom__contains=query)
        return render(request,"operations/fournisseur/rechercher.html",{"fournisseurs":fournisseurs})
    else :
        return render(request,"operations/fournisseur/rechercher.html")


###############################################################################################
################# ACHAT #########################################
#les views bon_commande
def save_bc_pdf(request,code):
        buffer = io.BytesIO()
        x = canvas.Canvas(buffer)
        bc = bon_commande.objects.filter(code_document=code)
        x.drawString(40, 800, "Le "+datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S").__str__())
        x.drawString(20, 750, "Code bon de commande : "+code.__str__())
        x.drawString(20, 725, "Nom                                                     Qte")
        x.drawString(20, 700, "-------------------------------------------------------------------")
        line=675
        for b in bc :
            x.drawString(20, line, b.contient.__str__() + "                  " +b.qte.__str__() )
            line-=20
        
        x.showPage()
        x.save()
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename='BonCommande.pdf')


def creer_bon_commande(request):
    if request.method == 'POST' :
        form=Creer_bon_commande(request.POST)
        if form.is_valid() :
            form.save()
            form=Creer_bon_commande()
            bc = bon_commande.objects.all()
            return render(request,"achat/creerbc.html",{"bc":bc,"form":form})
    else:
        form=Creer_bon_commande()
        bc = bon_commande.objects.all()
        return render(request,"achat/creerbc.html",{"bc":bc,"form":form})




def modifier_bon_commande(request,pk):
    try : 
        bc=bon_commande.objects.get(id=pk)
    except : 
        return redirect('bon_commandes')
    if request.method == 'POST' :
        form = Creer_bon_commande(request.POST,instance=bc)
        if form.is_valid() : 
            form.save()
            return redirect('bon_commandes')

    else :
        form=Creer_bon_commande(instance=bc)
        return render(request,'achat/modifierbc.html',{"form":form})




def supprimer_bon_commande(request,pk):
    bc=''
    if request.method == 'POST' :
        bc=bon_commande.objects.filter(code_document=pk)
        bc.delete()
        return redirect('bon_commandes')
    else :
        bc=bon_commande.objects.filter(code_document=pk)
        return render(request,'achat/supprimerbc.html',{"typep":bc})



###############################################################################################
#les views facture
def creer_facture(request):
    if request.method == 'POST' :
        form=Creer_facture(request.POST)
        if form.is_valid() :
            form.save()
            form=Creer_facture()
        return redirect('factures')
    else:
        form=Creer_facture()
        factures=facture.objects.all()
        return render(request,"achat/creerfacture.html",{"factures":factures,"form":form})



###############################################################################################
#les views bon livraison
def creer_bl(request):
    if request.method == 'POST' :
        form=Creer_bl(request.POST)
        if form.is_valid() :
            form.save()
            form=Creer_bl()
        return redirect('bls')
    else:
        form=Creer_bl()
        bls=bl.objects.all()
        return render(request,"achat/creerbl.html",{"bls":bls,"form":form})



#etat de stock de l'achat
def saisir_etat_stock(request,id):
        produits = bon_commande.objects.filter(code_document= id)
        return render(request,'achat/entree.html',{'prod':produits , 'id':id})




##########################################################################################################################
################# STOCK #########################################

#etat stock
def afficher_etat_stock(request):
    produits = produit.objects.all()
    return render(request,"stock/etatstock.html",{"produits":produits})