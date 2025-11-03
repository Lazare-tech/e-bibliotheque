from django.contrib import admin
from .models import Categorie, Auteur, Commentaire, Livre,MessageContact
from django.utils.html import format_html
###################################################################
@admin.register(Livre)
class LivreAdmin(admin.ModelAdmin):
    list_display = ('idlivre', 'titre', 'utilisateur', 'categorie', 'datepublication', 'afficher_couverture', 'nbtelechargement')
    list_filter = ('categorie', 'langue', 'statut', 'datepublication')
    search_fields = ('titre', 'auteur__nom', 'categorie__nom')
    readonly_fields = ('afficher_couverture',)
    ordering = ('-datepublication',)

    # Pour afficher la miniature de la couverture dans l’admin
    def afficher_couverture(self, obj):
        if obj.cover_image:
            return format_html('<img src="{}" width="60" height="80" style="object-fit: cover; border-radius: 4px;" />', obj.cover_image.url)
        return "(Pas de couverture)"
    afficher_couverture.short_description = "Couverture"
    
###################################################################
###################################################################
@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('idcategorie', 'nom', 'type')
    search_fields = ('nom', 'type')
    list_filter = ('type',)
    ordering = ('nom',)
    
###################################################################
@admin.register(Auteur)
class AuteurAdmin(admin.ModelAdmin):
    list_display = ('idauteur', 'nom', 'prenom', 'adresse')
    search_fields = ('nom', 'prenom', 'adresse')
    ordering = ('nom',)
    
###################################################################
@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('idcommentaire', 'livre', 'utilisateur', 'contenu', 'datecommentaire')
    list_filter = ('datecommentaire',)
    search_fields = ('contenu', 'utilisateur__username', 'livre__titre')
    ordering = ('-datecommentaire',)
    
###################################################################
@admin.register(MessageContact)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('expediteur', 'email', 'objet', 'date_envoi')
    search_fields = ('email', 'objet', 'contenu')
    list_filter = ('date_envoi',)
    readonly_fields = ('date_envoi',)
    ordering = ('-date_envoi',)