from django.shortcuts import render
from django.http import JsonResponse
from .models import Cocktail

def cocktailapi(request):
    
    cocktails = Cocktail.objects.all()
    return JsonResponse({"results":[
        {
            'name':cocktail.name,
            "root_cocktail":cocktail.root_cocktail,
            "primary_spirit":cocktail.primary_spirit,
            "recipe":cocktail.recipe,
            
         }for cocktail in cocktails
    ]})