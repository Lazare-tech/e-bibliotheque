
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from bibliotheque.views import home
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login 

class CustomLoginView(LoginView):
    template_name = 'login.html'  # Mets le chemin correct vers ton fichier

class CustomLogoutView(LogoutView):
    next_page = 'bibliotheque:homepage'  # Redirige vers la page de connexion après déconnexion
    
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        # Validation
        errors = []
        
        if not username or not password1 or not password2:
            errors.append("Tous les champs sont requis.")
        
        if password1 != password2:
            errors.append("Les mots de passe ne correspondent pas.")
        
        if len(password1) < 8:
            errors.append("Le mot de passe doit contenir au moins 8 caractères.")
        
        if User.objects.filter(username=username).exists():
            errors.append("Ce nom d'utilisateur existe déjà.")
        
        if email and User.objects.filter(email=email).exists():
            errors.append("Cet email est déjà utilisé.")
        
        # Si pas d'erreurs, créer l'utilisateur SIMPLE
        if not errors:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1,
                is_staff=False,        # Pas d'accès admin
                is_superuser=False     # Pas superutilisateur
            )
            
            return redirect('bibliotheque:login')
            messages.success(request, 'Compte créé avec succès !')
            return redirect('/')
        else:
            for error in errors:
                messages.error(request, error)
    
    return render(request, 'register.html')
##

def register(request):
    return render(request, 'register.html')
