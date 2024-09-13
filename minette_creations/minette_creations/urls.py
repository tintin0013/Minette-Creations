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
from django.contrib import admin
from django.urls import path
from listings import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('animaux/', views.animaux),  # Ajout d'une URL pour la page animaux
    path('doudou/', views.doudou),  # Ajout d'une URL pour la page doudou
    path('lapinou/', views.lapinou), # Ajout d'une URL pour la page lapinou
    path('porte-cles/', views.porteCles),  # Ajout d'une URL pour la page Porte-Cles
    path('artisanale/', views.artisanale), # Ajout d'une URL
    path('gourmande/', views.gourmande),  # Ajout d'une URL pour la page gourmande
    path('fondant/', views.fondant),  # Ajout d'une URL pour la page fondant
    path('fondantCremeux/', views.fondantCremeux), # Ajout d'une URL pour la page fondant Cremeux
    path('bruleurs/', views.bruleurs),  # Ajout d'une URL pour la page bruleurs

    path('about-us/', views.about),  # Ajout d'une URL pour la page A propos
    path('contact-us/', views.contact),  # Ajout d'une URL pour la page contact
    path('email_sent/', views.email_sent, name='email_sent'),
    # path('crochet/', views.crochet),
    # path('bougie/', views.bougie),
]
