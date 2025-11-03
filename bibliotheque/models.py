from django.db import models
from django.contrib.auth.models import User
from pdf2image import convert_from_path
from PIL import Image
import os
#
class Categorie(models.Model):
    idcategorie = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=100, null=True,blank=True)  
    
    def __str__(self):
        return self.nom


class Auteur(models.Model):
    idauteur = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100,null=True,blank=True)
    prenom = models.CharField(max_length=100, blank=True, null=True)
    adresse = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.nom


class Livre(models.Model):
    idlivre = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=200)
    format = models.CharField(max_length=200)
    statut = models.CharField(max_length=100)
    nbpage = models.IntegerField(blank=True, null=True)
    resume = models.CharField(max_length=100, blank=True, null=True)
    langue = models.CharField(max_length=100, blank=True, null=True)
    nbtelechargement = models.IntegerField(default=0)
    fichier = models.FileField(upload_to='fichiers/')
    datepublication = models.DateField(auto_now_add=True)
    cover_image = models.ImageField(upload_to='livres_couvertures/', blank=True, null=True)
    mentionjaime = models.IntegerField(default=0)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titre
    #

class Commentaire(models.Model):
    idcommentaire = models.AutoField(primary_key=True)
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    contenu = models.TextField()
    datecommentaire = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='reponses'
    )
    
    def __str__(self):
        return f"Commentaire de {self.utilisateur.username} sur {self.livre.titre}"

class MessageContact(models.Model):
    expediteur = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=200)
    objet = models.CharField(max_length=200)
    contenu = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message de {self.email} - {self.objet}"