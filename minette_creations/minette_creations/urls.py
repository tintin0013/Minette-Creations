"""
URL configuration for minette_creations project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from listings import views  


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello, name='hello'),
    path('animaux/', views.animaux, name='animaux'),  # Ajout d'une URL pour la page animaux
    path('doudou/', views.doudou, name='doudou'),  # Ajout d'une URL pour la page doudou
    path('lapinou/', views.lapinou, name='lapinou'), # Ajout d'une URL pour la page lapinou
    path('porte-cles/', views.porteCles, name='porteCles'),  # Ajout d'une URL pour la page Porte-Cles
    path('artisanale/', views.artisanale, name='artisanale'), # Ajout d'une URL
    path('gourmande/', views.gourmande, name='gourmande'),  # Ajout d'une URL pour la page gourmande
    path('fondant/', views.fondant, name='fondant'),  # Ajout d'une URL pour la page fondant
    path('fondantCremeux/', views.fondantCremeux, name='fondantCremeux'), # Ajout d'une URL pour la page fondant Cremeux
    path('bruleurs/', views.bruleurs, name='bruleurs'),  # Ajout d'une URL pour la page bruleurs

    path('about-us/', views.about, name='about'),  # Ajout d'une URL pour la page A propos
    path('contact-us/', views.contact, name='contact'),  # Ajout d'une URL pour la page contact
    path('email_sent/', views.email_sent, name='email_sent'),
    path('<str:categorie>/<int:id>/', views.afficher_image, name='afficher_image'),    # path('crochet/', views.crochet),
    # path('bougie/', views.bougie),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
