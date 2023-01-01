from django.contrib import admin
from django.urls import include,path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('login/',views.Verify_Login),
    path('login/stock/',views.Afficher_Stock),
    path('produits/',views.lister_produit,name='produits'),
    path('produits/modifier/<int:pk>',views.modifier_produit,name='modifier_produits'),
    path('produits/modifier/',RedirectView.as_view(url='/produits/')),
    path('produits/supprimer/<int:pk>',views.supprimer_produit,name='supprimer_produits'),
    path('produits/supprimer/',RedirectView.as_view(url='/produits/')),
]
