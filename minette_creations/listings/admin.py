from django.contrib import admin
from listings.models import CrochetAnimaux, CrochetDoudou, CrochetLapinou, CrochetPorteCles, BougieArtisanale,BougieGourmande, Fondant, FondantCremeux,Bruleurs


 # liste les champs que nous voulons sur l'affichage de la liste
class AnimauxAdmin(admin.ModelAdmin): 
    list_display = ('nom', 'description', 'couleur', 'taille', 'matiere')

class DoudouAdmin(admin.ModelAdmin): 
    list_display = ('nom', 'description', 'couleur', 'taille', 'matiere') 

class LapinouAdmin(admin.ModelAdmin): 
    list_display = ('nom', 'description', 'couleur', 'taille', 'matiere') 

class PorteClesAdmin(admin.ModelAdmin): 
    list_display = ('nom', 'description', 'couleur', 'taille', 'matiere') 

class ArtisanaleAdmin(admin.ModelAdmin): 
    list_display = ('nom', 'description', 'couleur', 'taille', 'forme') 

class GourmandeAdmin(admin.ModelAdmin): 
    list_display = ('nom', 'description', 'couleur', 'taille', 'forme') 

class FondantAdmin(admin.ModelAdmin): 
    list_display = ('nom', 'description', 'couleur', 'taille', 'forme') 

class FondantCremeuxAdmin(admin.ModelAdmin): 
    list_display = ('nom', 'description', 'couleur', 'taille', 'forme') 

class BruleursAdmin(admin.ModelAdmin): 
    list_display = ('nom', 'description', 'couleur', 'taille', 'forme') 


admin.site.register(CrochetAnimaux, AnimauxAdmin)
admin.site.register(CrochetDoudou, DoudouAdmin)
admin.site.register(CrochetLapinou, LapinouAdmin)
admin.site.register(CrochetPorteCles, PorteClesAdmin)
admin.site.register(BougieArtisanale, ArtisanaleAdmin)
admin.site.register(BougieGourmande, GourmandeAdmin)
admin.site.register(Fondant, FondantAdmin)
admin.site.register(FondantCremeux, FondantCremeuxAdmin)
admin.site.register(Bruleurs, BruleursAdmin)

# Register your models here.
