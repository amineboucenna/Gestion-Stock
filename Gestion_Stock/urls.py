from django.contrib import admin
from django.urls import include,path
from . import views

urlpatterns = [
    path('login/',views.Verify_Login),
    path('login/stock/',views.Afficher_Stock),
]
