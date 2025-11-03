from django.shortcuts import render
from .models import Categorie
#
def categorie_processor(request):
    categorie= Categorie.objects.all()
    context={
        'categorie':categorie
    }
    return context