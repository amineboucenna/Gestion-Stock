from django.shortcuts import redirect, render
from .models import Comptes,produit
# Create your views here.


def Verify_Login(request):
    if request.method == "GET" : 
        accountquery=request.GET.get('usernameinput')      
        if accountquery :
            database_username=Comptes.objects.filter(username = accountquery )   
            passwordquery=request.GET.get('passwordinput')
            if database_username :
                if database_username[0].username == accountquery and database_username[0].password == passwordquery :
                    return redirect('stock/')
                else :
                    msg = 'Incorrect username or password'
                    return render(request,"login.html",{"msg":msg})
            else :
                msg = 'The user given does not exist'
                return render(request,"login.html",{"msg":msg})
        else :
            return render(request,"login.html")




def Afficher_Stock(request):
    #a completer apres la creation de MCD
    return render(request,"index.html")



def testing(request):
    return render(request,"test.html")


def lololo(request):
    return render(request,"partials/file.html")

def Logout(request):
    return render(request,"login.html")

def lister_produit(request):
    prod = produit.objects.all()
    return render(request,"operations/liste_produit.html",{"prod":prod})


def modifier_produit(request,pk):
    prd=''
    try : 
        prd=produit.objects.get(id=pk)
    except : 
        return redirect('produits')
    if request.method == 'POST' :
        form = produit(request.POST,pk=prd)
        if form.is_valid() : 
            form.save()
            return redirect('produits')
    else :
        form=produit(pk=prd)
        return render(request,'operations/modifier_produit.html',{"form":form})


def supprimer_produit(request,pk):
    prd=''
    try : 
        prd=produit.objects.get(id=pk)
    except : 
        lister_produit(request)
    if request.method == 'POST' :
        prd=produit.objects.get(id=pk)
        prd.delete()
        redirect(request,'produits')
    else :
        return render(request,'operations/supprimer_produit.html')