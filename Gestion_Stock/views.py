#imports for generating pdf file

import datetime
import io
from reportlab.pdfgen import canvas

from django.http import FileResponse
from django.shortcuts import redirect, render

#imports for views

from .forms import (Creer_bl, Creer_bon_commande, Creer_client, Creer_facture,
                    Creer_fournisseur, Creer_produit, Creer_typep,Creer_entree_S,Creer_sortie_S,Creer_vente)
from .models import (Comptes, bl, bon_commande, client, facture, fournisseur,
                     produit, type_produit , achat_entree_stock , reglement , stock , sortie_stock,vente)



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
    if request.method == "GET" :
        query=request.GET.get("rechercher")
        if query : 
            prod=produit.objects.filter(type_produit_id=query)
        return render(request,"operations/produit/rechercher_type_produit.html",{"prod":prod})
    else :
        return render(request,"operations/produit/rechercher_type_produit.html")



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
            for c in b.contient.all() :
                x.drawString(20, line, c.designation.__str__() + "                  " +b.qte.__str__() )
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



def supprimer_bl(pk):
    delete_bl = bl.objects.filter(pk=pk)
    delete_bl.delete()
    redirect('bls')



#etat de stock de l'achat
def saisir_etat_stock(request,id):
        
    selected_bon_commande = bon_commande.objects.filter(code_document=id)
    for s in selected_bon_commande :
        for c in s.contient.all() :
            ach = achat_entree_stock()
            ach.id_commande = s
            ach.id_produit = c.pk
            ach.qte = 0 
            ach.prix_achat = 0
            ach.prix_vente = 0
            ach.tot = ach.prix_achat * ach.qte
            ach.save()
    selected_entree_stock= achat_entree_stock.objects.all()
    return render(request,'achat/entree.html',{'selected_bc':selected_entree_stock, 'id':id})




def inserer_etat_stock(request,pk,id):
    entree_s=achat_entree_stock.objects.get(id=pk)
    if request.method == 'POST' :
        form=Creer_entree_S(request.POST,instance=entree_s)
        if form.is_valid() :
            form.save()
            form=Creer_entree_S()
            select_es = achat_entree_stock.objects.get(id=pk)
            select_es.tot = select_es.qte * select_es.prix_achat
            select_es.save()
        select_es = achat_entree_stock.objects.all()
        return render(request,'achat/entree.html',{'selected_bc':select_es , 'id':id })
    else:
        form=Creer_entree_S(instance=entree_s)
        return render(request,"achat/creerentree.html",{"form":form})


#reglement

def gerer_reglement(request,id):
    reg=''
    if not reglement.objects.filter(code_bon_livraison = bl.objects.get(pk=id)) :
        r = reglement()
        r.code_bon_livraison = bl.objects.get(pk=id)
        r.nom_fournisseur = bl.objects.get(pk=id).bl_avoir.nom + ' ' + bl.objects.get(pk=id).bl_avoir.prenom
        total_ht = 0
        for e in achat_entree_stock.objects.all() : 
            total_ht = total_ht + e.tot
        r.prix_reglement_bl = total_ht
        r.prix_reglement_facture = total_ht - ( total_ht * 0.19 )
        r.save()
    else :
        reg = reglement.objects.all()
    return render(request,'achat/reglement.html',{'reglement':reg}) 





def supprimer_reglement(pk):
    reglement_supprimer = reglement.objects.filter(pk=pk)
    reglement_supprimer.delete()
    redirect('bls')


##########################################################################################################################
################# STOCK #########################################

#entree stock



def afficher_entree_stock(request):
    selected_es = achat_entree_stock.objects.all()
    return render(request,'stock/entrer.html',{'selected_es':selected_es})


def enfiler_stock(request,pk):
    e = achat_entree_stock.objects.get(id=pk)
    s = stock()
    s.id_produit = e.id_produit
    s.qte = e.qte
    s.prix_achat = e.prix_achat
    s.prix_vente = e.prix_vente
    s.save()   
    selected_es = achat_entree_stock.objects.all()
    return render(request,'stock/entrer.html',{'selected_es':selected_es})


#etat stock
def afficher_etat_stock(request):
    produits_stock = stock.objects.all()
    total_achat = 0
    total_vente = 0
    for p in produits_stock : 
        total_achat = p.prix_achat * p.qte
        total_vente = p.prix_vente * p.qte
    diff = total_vente - total_achat
    return render(request,"stock/etatstock.html",{"produits_stock":produits_stock,'total_achat':total_achat,'total_vente':total_vente,'diff':diff})


def imprimer_etat_stock(request):
        buffer = io.BytesIO()
        x = canvas.Canvas(buffer)
        op_stock = stock.objects.all()
        x.drawString(40, 800, "Le "+datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S").__str__())
        x.drawString(20, 750, "La liste de produit en Stock : ")
        x.drawString(20, 725, "Code Produit | Nom Produit | Qte |  Date Saisie | Prix d'achat | Prix de vente")
        x.drawString(20, 700, "------------------------------------------------------------------------------------------------------")
        line=675
        for s in op_stock :
            p = produit.objects.get(pk=s.pk)
            x.drawString(20, line, p.pk.__str__() +" | "+ p.designation.__str__() +" | " +s.qte.__str__()+" | "+s.date_saisie.strftime("%d-%m-%Y %H:%M:%S").__str__()+" | "+s.prix_achat.__str__()+" | "+s.prix_vente.__str__() )
            line-=20
        x.showPage()
        x.save()
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename='EtatStock.pdf')

#sortie stock
def defiler_stock(request,pk):
    get_a_supprimer=stock.objects.get(id=pk)
    if request.method == 'POST' :
        form = Creer_sortie_S(request.POST,instance=get_a_supprimer)
        if form.is_valid() : 
            form.save()
            last_sortie = sortie_stock.objects.get(pk=pk)
            #get_a_supprimer.qte = get_a_supprimer.qte - last_sortie.qte_a_enlever
            get_a_supprimer.save()
            return redirect('afficher_sortie_stock')
    else :
        form= Creer_sortie_S(request.POST,instance=get_a_supprimer)
        return render(request,'stock/inserersortiestock.html',{"form":form})


def afficher_sortie_stock(request):
    sortie_s = sortie_stock.objects.all()
    return render(request,'stock/sortiestock.html',{"sortie_s":sortie_s})
    


#vente 
def lister_vente(request):
    if request.method == 'POST' :
        form=Creer_vente(request.POST)
        if form.is_valid() :
            form.save()
            form=Creer_vente()
            ventes = vente.objects.all()
            return render(request,"vente/ventecomptoir.html",{"vente":ventes,"form":form})
        form=Creer_typep(request.POST)
        if form.is_valid() :
            form.save()
            form=Creer_vente()
            ventes = vente.objects.all()
            return render(request,"vente/ventecomptoir.html",{"vente":ventes,"form":form})
    else:
        form=Creer_vente()
        ventes = vente.objects.all()
        return render(request,"vente/ventecomptoir.html",{"vente":ventes,"form":form})

 