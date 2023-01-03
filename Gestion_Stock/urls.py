from django.contrib import admin
from django.urls import include,path
from . import views
from django.views.generic import RedirectView

urlpatterns = [

    #login functions
    path('login/',views.Verify_Login),
    path('login/stock/',views.Afficher_Stock),

    #Remarque : 
        #
        #
        #

    #model produit
    path('login/produits/',views.lister_produit,name='produits'),
    path('login/produits/modifier/<int:pk>',views.modifier_produit,name='modifier_produits'),
    path('login/produits/modifier/',RedirectView.as_view(url='/produits/')),
    path('login/produits/supprimer/<int:pk>',views.supprimer_produit,name='supprimer_produits'),
    path('login/produits/supprimer/',RedirectView.as_view(url='/produits/')),
    path('login/produits/rechercher/',views.rechercher_produit,name='rechercher_produit'),
    path('login/produits/rechercher/',views.rechercher_type_produit,name='rechercher_type_produit'),
    path('login/produits/rechercher/',views.rechercher_typep_produit,name='rechercher_typep_produit'),


    #model typeproduit
    #remarque l'affichage de type produit a ete fait avec l'affichage de produit
    path('login/produits/modifiertype/<int:pk>',views.modifier_type_produit,name='modifier_typeproduit'),
    path('login/produits/modifiertype/',RedirectView.as_view(url='/produits/')),
    path('login/produits/supprimertype/<int:pk>',views.supprimer_type_produit,name='supprimer_typeproduit'),
    path('login/produits/supprimertype/',RedirectView.as_view(url='/produits/')),


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

    ########################################################################################################################
    #   SECTION ACHAT
    #model bon_commande
    path('login/achat/bon_commande/',views.creer_bon_commande,name='bon_commandes'),
    path('login/achat/modifier_bon_commande/<int:pk>',views.modifier_bon_commande,name='modifier_bon_commandes'),
    path('login/achat/supprimer_bon_commande/<int:pk>',views.supprimer_bon_commande,name='supprimer_bon_commandes'),
    path('login/achat/modifier_bon_commande/',RedirectView.as_view(url='/bon_commandes/')),
    path('login/achat/supprimer_bon_commande/',RedirectView.as_view(url='/bon_commandes/')),

    #model facutre
    path('login/achat/facture/',views.creer_facture,name='factures'),


    #model bonlivraison
    path('login/achat/bonlivraison/',views.creer_bl,name='bls'),

]
