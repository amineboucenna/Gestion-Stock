from django.shortcuts import redirect, render
from .models import Comptes
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


def Logout(request):
    return render(request,"login.html")