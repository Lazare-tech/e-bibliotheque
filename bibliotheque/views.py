from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Categorie, Auteur, Livre, Commentaire, MessageContact
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .forms import LivreForm,ContactForm
# Create your views here.
def home(request):
    livres = Livre.objects.all()
    auteur = Auteur.objects.all()
    commentaire = Commentaire.objects.all()
    context={
        'livres': livres,
    }
    return render(request, 'bibliotheque/body/home.html',context)
####

def test_404(request, exception):
    """
    Vue personnalisée pour les erreurs 404.
    Affiche une belle page avec le template 404.html.
    """
    return render(request, '404.html', status=404)

def faq(request):
    return render(request, 'bibliotheque/body/faq.html')
###

def help(request):
    return render(request, 'bibliotheque/body/aide.html')
#################################################################################################################
def mon_espace(request):
    mes_soumissions = Livre.objects.filter(utilisateur__username=request.user.username).count()
    mes_livres = Livre.objects.filter(utilisateur=request.user).order_by('-datepublication')
    categories_user = mes_livres.values_list('categorie', flat=True)
    livres_recommandes = Livre.objects.filter(
        categorie__in=categories_user
    ).exclude(utilisateur=request.user).distinct()[:8]  

    livres = Livre.objects.all().count()
    auteurs = Auteur.objects.all()
    categories = Categorie.objects.all()
    if request.method == 'POST':
        form = LivreForm(request.POST, request.FILES)
        if form.is_valid():
            livre = form.save(commit=False)
            livre.utilisateur = request.user  
            livre.save()
            messages.success(request, "Livre ajouté avec succès !")
            return redirect('bibliotheque:mon_espace')  # à adapter à ton URL
        else:
            messages.error(request, "Une erreur est survenue. Vérifiez le formulaire.")
    else:
        form = LivreForm()

    return render(request, 'bibliotheque/body/my_space.html', {
        'mes_livres': mes_livres,
        'mes_soumissions': mes_soumissions,
        'auteurs': auteurs,
        'categories': categories,
        'livres': livres,
        'form':form,
        'livres_recommandes': livres_recommandes,
    })
####
@login_required
def supprimer_livre(request, livre_id):
    livre = get_object_or_404(Livre, id=livre_id, utilisateur=request.user)
    livre.delete()
    return redirect('bibliotheque:mon_espace')
###
@login_required
def lire_livre(request, livre_id):
    livre = get_object_or_404(Livre, idlivre=livre_id, utilisateur=request.user)
    return render(request, 'bibliotheque/body/lire_livre.html', {'livre': livre})

#######################################################################################################################
def details(request, id):
    livre = get_object_or_404(Livre, idlivre=id)
    Commentaires=Commentaire.objects.filter(livre=livre).order_by('-datecommentaire')
    categorie = livre.categorie
    livres_similaires = Livre.objects.filter(categorie=categorie).exclude(idlivre=livre.idlivre)[:4]
    context={
        'livre':livre,
        'commentaires':Commentaires,
        'livres_similaires':livres_similaires,
    }
    # Passer le livre au template
    return render(request, 'bibliotheque/body/details.html', context)
###
#####
def my_contact(request):
    erreur = None

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # On récupère les données nettoyées du formulaire
            objet = form.cleaned_data['objet']
            contenu = form.cleaned_data['contenu']

            # Création du message avec l'utilisateur connecté
            MessageContact.objects.create(
                expediteur=request.user,
                email=request.user.email,
                objet=objet,
                contenu=contenu
            )
            messages.success(request, "Votre message a été envoyé avec succès. Merci de nous avoir contactés !")
            # return redirect('bibliotheque:contact_success')
        else:
            erreur = "Veuillez remplir correctement le formulaire."
    else:
        form = ContactForm()

    return render(request, 'bibliotheque/body/contact.html', {
        'form': form,
        'erreur': erreur
    })

#logique applicative
@csrf_exempt
@login_required
def ajouter_categorie(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        type = request.POST.get('type')
        
        if not nom:
            return render(request, '', {'erreur': 'Le nom est requis'})
        
        Categorie.objects.create(nom=nom, type=type)
        return redirect('mon_espace')  # redirection vers la liste des catégories

@csrf_exempt
@login_required
def ajouter_livre(request):
    if request.method == 'POST':
        form = LivreForm(request.POST, request.FILES)
        if form.is_valid():
            livre = form.save(commit=False)
            livre.utilisateur = request.user  
            livre.save()
            messages.success(request, "Livre ajouté avec succès !")
            return redirect('bibliotheque:mon_espace')  # à adapter à ton URL
        else:
            messages.error(request, "Une erreur est survenue. Vérifiez le formulaire.")
    else:
        form = LivreForm()

    return render(request, 'bibliotheque/body/my_space.html', {'form': form})

###

# def recherche_livres(request):
#     query = request.GET.get('query', '')
#     categorie_id = request.GET.get('categorie', '')

#     livres = Livre.objects.all()

#     # Filtrage par mot-clé
#     if query:
#         livres = livres.filter(
#             titre__icontains=query
#         ) | livres.filter(auteur__icontains=query)

#     # Filtrage par catégorie
#     if categorie_id:
#         livres = livres.filter(categorie__idcategorie=categorie_id)

#     categories = Categorie.objects.all()

#     return render(request, 'bibliotheque/body/home.html', {
#         'livres': livres,
#         'categorie': categories,
#         'query': query,
#     })
from django.db.models import Q

def recherche_livres(request):
    query = request.GET.get('query', '').strip()
    categorie_id = request.GET.get('categorie', '').strip()

    livres = Livre.objects.all()

    if query:
        livres = livres.filter(
            Q(titre__icontains=query) |
            Q(auteur__nom__icontains=query)
        )

    if categorie_id:
        livres = livres.filter(categorie__idcategorie=categorie_id)

    categories = Categorie.objects.all()

    return render(request, 'bibliotheque/body/home.html', {
        'livres': livres,
        'categorie': categories,
        'query': query,
        'categorie_id': categorie_id,
    })

######
@login_required
def ajouter_auteur(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        adresse = request.POST.get('adresse')
        
        if not nom:
            return render(request, '', {'erreur': 'Le nom est requis'})
        
        Auteur.objects.create(nom=nom, prenom=prenom, adresse=adresse)
        return redirect('mon_espace')  # redirection vers la liste des auteurs
    
    return render(request, 'bibliotheque:mon_espace')
###################################################################################################
@login_required
def ajouter_commentaire(request, idlivre):
    livre = get_object_or_404(Livre, pk=idlivre)
    parent_id = request.POST.get('parent_id')  # si c’est une réponse
    
    if request.method == 'POST':
        contenu = request.POST.get('contenu')
        
        parent = None
        if parent_id:
            parent = Commentaire.objects.get(idcommentaire=parent_id)

        
        Commentaire.objects.create(
            livre=livre,
            utilisateur=request.user,  # si ton modèle a 'nom_utilisateur'
            contenu=contenu,
             parent=parent,
             
        )
        return redirect('bibliotheque:details', id=livre.idlivre)  # renvoie vers la page du livre
    
    return render(request, '', {'livre': livre})
####
def supprimer_commentaire(request, idcommentaire):
    commentaire = get_object_or_404(Commentaire, pk=idcommentaire)
    
    if request.method == 'POST':
        idlivre = commentaire.livre.idlivre
        commentaire.delete()
        return redirect('details', id=idlivre)
####
@login_required
def modifier_commentaire(request, idcommentaire):
    commentaire = get_object_or_404(Commentaire, idcommentaire=idcommentaire, utilisateur=request.user)

    if request.method == 'POST':
        nouveau_contenu = request.POST.get('contenu')
        commentaire.contenu = nouveau_contenu
        commentaire.save()
        return redirect('bibliotheque:details', id=commentaire.livre.idlivre)
###################################################################################################

#suppression
def supprimer_livre(request, idlivre):
    livre = get_object_or_404(Livre, pk=idlivre)
    
    if request.method == 'POST':
        livre.delete()
        return redirect('home')
    
    
def supprimer_auteur(request, idauteur):
    auteur = get_object_or_404(Auteur, pk=idauteur)
    
    if request.method == 'POST':
        auteur.delete()
        return redirect('home')
    
def supprimer_categorie(request, idcategorie):
    categorie = get_object_or_404(Categorie, pk=idcategorie)
    
    if request.method == 'POST':
        categorie.delete()
        return redirect('home')
    

    
def mentionjaime(request, idlivre):
    livre = get_object_or_404(Livre, pk=idlivre)
    livre.mentionjaime += 1
    livre.save()
    return redirect('detail_livre', idlivre=idlivre)


@login_required
def contacter_admin(request):
    if request.method == 'POST':
        objet = request.POST.get('objet')
        contenu = request.POST.get('contenu')

        if objet and contenu:
            MessageContact.objects.create(
                expediteur=request.user,
                email=request.user.email,
                objet=objet,
                contenu=contenu
            )
            return render(request, 'bibliotheque/body/home.html')
        else:
            erreur = "Veuillez remplir tous les champs."
            return render(request, 'bibliotheque/body/contacter_admin.html', {'erreur': erreur})

    return render(request, 'bibliotheque/body/contacter_admin.html')

def messages_admin(request):
    messages = MessageContact.objects.all().order_by('-date_envoi')
    return render(request, 'bibliotheque/body/messages_admin.html', {'messages': messages})