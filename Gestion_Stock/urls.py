from django.contrib import admin
from django.urls import include,path
from . import views
from django.views.generic import RedirectView

urlpatterns = [

    #login functions
    path('login/',views.Verify_Login),
    path('login/stock/',views.Afficher_Stock),

    #model produit
    path('login/produits/',views.lister_produit,name='produits'),
    path('login/produits/modifier/<int:pk>',views.modifier_produit,name='modifier_produits'),
    path('login/produits/modifier/',RedirectView.as_view(url='/produits/')),
    path('login/produits/supprimer/<int:pk>',views.supprimer_produit,name='supprimer_produits'),
    path('login/produits/supprimer/',RedirectView.as_view(url='/produits/')),
    path('login/produits/rechercher/',views.rechercher_produit,name='rechercher_produit'),
    path('login/produits/rechercher/',views.rechercher_type_produit,name='rechercher_type_produit'),
    path('login/produits/rechercher/',views.rechercher_typep_produit,name='rechercher_typep_produit'),

    #model Client
    path('login/clients/',views.lister_client,name='clients'),
    path('login/clients/modifier/<int:pk>',views.modifier_client,name='modifier_clients'),
    path('login/clients/modifier/',RedirectView.as_view(url='/clients/')),
    path('login/clients/supprimer/<int:pk>',views.supprimer_client,name='supprimer_clients'),
    path('login/clients/supprimer/',RedirectView.as_view(url='/clients/')),
    path('login/clients/rechercher/',views.rechercher_client,name='rechercher_clients'),


    #model fournisseur
    path('login/fournisseurs/',views.lister_fournisseur,name='fournisseurs'),
    path('login/fournisseurs/modifier/<int:pk>',views.modifier_fournisseur,name='modifier_fournisseurs'),
    path('login/fournisseurs/modifier/',RedirectView.as_view(url='/fournisseurs/')),
    path('login/fournisseurs/supprimer/<int:pk>',views.supprimer_fournisseur,name='supprimer_fournisseurs'),
    path('login/fournisseurs/supprimer/',RedirectView.as_view(url='/fournisseurs/')),
    path('login/fournisseurs/rechercher/',views.rechercher_fournisseur,name='rechercher_fournisseurs'),

     



]
