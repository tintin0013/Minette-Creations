
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import redirect 
from listings.models import CrochetAnimaux, CrochetDoudou, CrochetLapinou, CrochetPorteCles, BougieArtisanale,BougieGourmande, Fondant, FondantCremeux,Bruleurs
# from listings.forms import ContactUsForm, BandForm, ListingForm


def hello(request):
    crochetsAnimaux = CrochetAnimaux.objects.all()
    return render(request, 'listings/hello.html')


def animaux(request):
    crochetAnimaux = CrochetAnimaux.objects.all()
    return render(request, 'listings/animaux.html', {'crochetAnimaux': crochetAnimaux})


def doudou(request):
    crochetDoudou = CrochetDoudou.objects.all()
    return render(request, 'listings/doudou.html', {'crochetDoudou': crochetDoudou})


def lapinou(request):
    crochetLapinou = CrochetLapinou.objects.all()
    return render(request, 'listings/lapinou.html', {'crochetLapinou': crochetLapinou})


def porteCles(request):
    crochetPorteCles = CrochetPorteCles.objects.all()
    return render(request, 'listings/porte-cles.html', {'crochetPorteCles': crochetPorteCles})

def artisanale(request):
    bougieArtisanale = BougieArtisanale.objects.all()
    return render(request, 'listings/artisanale.html', {'bougieArtisanale': bougieArtisanale})


def gourmande(request):
    bougieGourmande = BougieGourmande.objects.all()
    return render(request, 'listings/gourmande.html', {'bougieGourmande': bougieGourmande})


def fondant(request):
    fondant = Fondant.objects.all()
    return render(request, 'listings/fondant.html', {'fondant': fondant})


def fondantCremeux(request):
    fondantCremeux = FondantCremeux.objects.all()
    return render(request, 'listings/fondantCremeux.html', {'fondantCremeux': fondantCremeux})


def bruleurs(request):
    bruleurs = Bruleurs.objects.all()
    return render(request, 'listings/bruleurs.html', {'bruleurs': bruleurs})

def contact(request):
    return render(request, 'listings/contact.html')

def about(request):
    return render(request,
                  'listings/about.html')

def email_sent(request):
    return render(request, 'listings/email_sent.html')

# def sidebar(request):
#     return render(request, 'listings/sidebar.html')


# def contact(request):
#     print('La méthode de requête est : ', request.method)
#     print('Les données POST sont : ', request.POST)
#     if request.method == 'POST':
#      # créer une instance de notre formulaire et le remplir avec les données POST
#         form = ContactUsForm(request.POST)
#         if form.is_valid():
#             send_mail(
#             subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
#             message=form.cleaned_data['message'],
#             from_email=form.cleaned_data['email'],
#             recipient_list=['admin@merchex.xyz'],
#         )
#         return redirect('email_sent')    
#     # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
#     # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).
            
#     else:
#         # ceci doit être une requête GET, donc créer un formulaire vide
#         form = ContactUsForm()

#     return render(request,
#         'listings/contact.html',
#         {'form': form})


