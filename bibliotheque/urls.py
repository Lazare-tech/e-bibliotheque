from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
import bibliotheque.views
# Gestion de l'erreur 404

app_name = "bibliotheque"

urlpatterns = [
    path('Acceuil', bibliotheque.views.home, name='homepage'),
        path('faq/', bibliotheque.views.faq, name='faq'),
                path('contact/', bibliotheque.views.my_contact, name='contact'),
                path('', bibliotheque.views.help, name='aide'),
    path('error/', bibliotheque.views.test_404),
        path('details/<int:id>/', bibliotheque.views.details, name='details'),
        path('ajouter_categorie/', bibliotheque.views.ajouter_categorie, name='ajouter_categorie'),
# LIVRE_PATHS 
        path('mon_espace/', bibliotheque.views.mon_espace, name='mon_espace'),

        path('ajouter_livre/', bibliotheque.views.ajouter_livre, name='ajouter_livre'),
        path('supprimer/<int:livre_id>/', bibliotheque.views.supprimer_livre, name='supprimer_livre'),
        path('lire/<int:livre_id>/', bibliotheque.views.lire_livre, name='lire_livre'),
        path('recherche/', bibliotheque.views.recherche_livres, name='recherche_livres'),

#Commentaire paths
path('modifier_commentaire/<int:idcommentaire>/', bibliotheque.views.modifier_commentaire, name='modifier_commentaire'),
        path('ajouter_auteur/', bibliotheque.views.ajouter_auteur, name='ajouter_auteur'),
        path('ajouter_commentaire/<int:idlivre>/', bibliotheque.views.ajouter_commentaire, name='ajouter_commentaire'),
        path('supprimer_auteur/<int:idauteur>/', bibliotheque.views.supprimer_auteur, name='supprimer_auteur'),
        path('supprimer_categorie/<int:idcategorie>/', bibliotheque.views.supprimer_categorie, name='supprimer_categorie'),
        path('supprimer_commentaire/<int:idcommentaire>/', bibliotheque.views.supprimer_commentaire, name='supprimer_commentaire'),
        path('contacter-admin/', bibliotheque.views.contacter_admin, name='contacter_admin'),
        path('messages-admin/', bibliotheque.views.messages_admin, name='messages_admin'),
      
 
] +   static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Serve static and media files during development
