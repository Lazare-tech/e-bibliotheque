from django import forms
from .models import Livre,MessageContact

class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = [
            'titre', 'statut', 'langue', 'nbpage', 'resume',
            'categorie', 'fichier', 'cover_image'
        ]
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre du livre'}),
            'statut': forms.Select(choices=[('Publié', 'Publié'), ('Brouillon', 'Brouillon')], attrs={'class': 'form-select'}),
            'langue': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Français, Anglais...'}),
            'nbpage': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'resume': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'categorie': forms.Select(attrs={'class': 'form-select'}),
            'fichier': forms.FileInput(attrs={'class': 'form-control', 'accept': '.pdf,.doc,.docx,.epub'}),
            'cover_image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
        }
###

class ContactForm(forms.ModelForm):
    class Meta:
        model = MessageContact
        fields = ['objet', 'contenu']
        widgets = {
            'objet': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Quel est le sujet de votre message ?',
                'required': True
            }),
            'contenu': forms.Textarea(attrs={
                'class': 'form-control form-textarea',
                'placeholder': 'Décrivez votre demande en détail...',
                'rows': 5,
                'required': True
            }),
        }
