
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from django.core.mail import send_mail
from django.shortcuts import redirect 
from listings.models import CrochetAnimaux, CrochetDoudou, CrochetLapinou, CrochetPorteCles, BougieArtisanale,BougieGourmande, Fondant, FondantCremeux,Bruleurs
from listings.forms import ContactUsForm


def hello(request):
    return render(request,
                  'listings/hello.html')


def animaux(request):
    tous_objets = CrochetAnimaux.objects.all()
    print(tous_objets)  # Affiche les objets dans la console
    return render(request, 'listings/animaux.html', {'tous_objets': tous_objets})


def doudou(request):
    tous_objets = CrochetDoudou.objects.all()
    return render(request, 'listings/doudou.html', {'tous_objets': tous_objets})


def lapinou(request):
    tous_objets = CrochetLapinou.objects.all()
    return render(request, 'listings/lapinou.html', {'tous_objets': tous_objets})


def porteCles(request):
    tous_objets = CrochetPorteCles.objects.all()
    return render(request, 'listings/porte-cles.html', {'tous_objets': tous_objets})

def artisanale(request):
    tous_objets = BougieArtisanale.objects.all()
    return render(request, 'listings/artisanale.html', {'tous_objets': tous_objets})


def gourmande(request):
    tous_objets = BougieGourmande.objects.all()
    return render(request, 'listings/gourmande.html', {'tous_objets': tous_objets})


def fondant(request):
    tous_objets = Fondant.objects.all()
    return render(request, 'listings/fondant.html', {'tous_objets': tous_objets})


def fondantCremeux(request):
    tous_objets = FondantCremeux.objects.all()
    return render(request, 'listings/fondantCremeux.html', {'tous_objets': tous_objets})


def bruleurs(request):
    tous_objets = Bruleurs.objects.all()
    return render(request, 'listings/bruleurs.html', {'tous_objets': tous_objets})

def contact(request):
   if request.method == 'POST':
     # créer une instance de notre formulaire et le remplir avec les données POST
       form = ContactUsForm(request.POST)
       if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via Minette Créations Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@minetteCreations.fr'],
        )
       return redirect('email_sent')  # ajoutez cette instruction de retour
   else:
 # ceci doit être une requête GET, donc créer un formulaire vide
       form = ContactUsForm()

   return render(request,
        'listings/contact.html',
        {'form': form})

def about(request):
    return render(request,
                  'listings/about.html')

def email_sent(request):
    return render(request, 'listings/email_sent.html')



MODELS_DICT = {
    'crochetanimaux': CrochetAnimaux,
    'crochetdoudou': CrochetDoudou,
    'crochetlapinou': CrochetLapinou,
    'crochetportecle': CrochetPorteCles,
    'bougieartisanale': BougieArtisanale,
    'bougiegourmande': BougieGourmande,
    'fondant': Fondant,
    'fondantcremeux': FondantCremeux,
    'bruleurs': Bruleurs,
}


def afficher_image(request, categorie):
    # Récupérer le modèle correspondant à la catégorie
    model = MODELS_DICT.get(categorie.lower())
    if not model:
        return render(request, '404.html')  # Renvoyer une erreur 404 si la catégorie est invalide
    
    # Récupérer tous les objets de cette catégorie
    tous_objets = model.objects.all()
    
    # Déterminer le template à utiliser en fonction de la catégorie
    template_mapping = {
        'crochetanimaux': 'listings/animaux.html',
        'crochetdoudou': 'listings/doudou.html',
        'crochetlapinou': 'listings/lapinou.html',
        'crochetportecle': 'listings/porte-cles.html',
        'bougieartisanale': 'listings/artisanale.html',
        'bougiegourmande': 'listings/gourmande.html',
        'fondant': 'listings/fondant.html',
        'fondantcremeux': 'listings/fondantCremeux.html',
        'bruleurs': 'listings/bruleurs.html',
    }
    
    template = template_mapping.get(categorie.lower())
    if not template:
        return render(request, '404.html')  # Gestion d'erreur si le template n'est pas trouvé

    # Retourner le template en passant tous les objets
    return render(request, template, {'tous_objets': tous_objets})


def afficher_image(request, categorie, id):
    model = MODELS_DICT.get(categorie.lower())
    if not model:
        return render(request, '404.html')
    
    objet = get_object_or_404(model, id=id)
    
    return render(request, 'listings/afficher_image.html', {'objet': objet, 'categorie': categorie})




# def afficher_image(request, categorie, id):
#     # Récupérer le modèle correspondant à la catégorie
#     model = MODELS_DICT.get(categorie.lower())
#     if not model:
#         return render(request, '404.html')  # Renvoyer une erreur 404 si la catégorie est invalide
    
#     # Récupérer l'objet correspondant à l'ID
#     objet = get_object_or_404(model, id=id)
    
#     # Retourner le template en passant l'objet et la catégorie
#     return render(request, 'afficher_image.html', {'objet': objet, 'categorie': categorie})
