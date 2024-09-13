from django.db import models


class CrochetAnimaux(models.Model):
    nom = models.fields.CharField(max_length=50)
    description = models.fields.TextField(max_length=200)
    couleur = models.fields.CharField(max_length=20)
    taille = models.fields.CharField(max_length=20)
    matiere = models.fields.CharField(max_length=20)
    def __str__(self):
        return f'{self.nom}'


class CrochetDoudou(models.Model):
    nom = models.fields.CharField(max_length=50)
    description = models.fields.TextField(max_length=200)
    couleur = models.fields.CharField(max_length=20)
    taille = models.fields.CharField(max_length=20)
    matiere = models.fields.CharField(max_length=20)
    def __str__(self):
        return f'{self.nom}'

class CrochetLapinou(models.Model):
    nom = models.fields.CharField(max_length=50)
    description = models.fields.TextField(max_length=200)
    couleur = models.fields.CharField(max_length=20)
    taille = models.fields.CharField(max_length=20)
    matiere = models.fields.CharField(max_length=20)
    def __str__(self):
        return f'{self.nom}'

class CrochetPorteCles(models.Model):
    nom = models.fields.CharField(max_length=50)
    description = models.fields.TextField(max_length=200)
    couleur = models.fields.CharField(max_length=20)
    taille = models.fields.CharField(max_length=20)
    matiere = models.fields.CharField(max_length=20)
    def __str__(self):
        return f'{self.nom}'


class BougieArtisanale(models.Model):
    nom = models.fields.CharField(max_length=50)
    description = models.fields.TextField(max_length=200)
    couleur = models.fields.CharField(max_length=20)
    taille = models.fields.CharField(max_length=20)
    forme = models.fields.CharField(max_length=50)
    def __str__(self):
        return f'{self.nom}'

class BougieGourmande(models.Model):
    nom = models.fields.CharField(max_length=50)
    description = models.fields.TextField(max_length=200)
    couleur = models.fields.CharField(max_length=20)
    taille = models.fields.CharField(max_length=20)
    forme = models.fields.CharField(max_length=50)
    def __str__(self):
        return f'{self.nom}'

class Fondant(models.Model):
    nom = models.fields.CharField(max_length=50)
    description = models.fields.TextField(max_length=200)
    couleur = models.fields.CharField(max_length=20)
    taille = models.fields.CharField(max_length=20)
    forme = models.fields.CharField(max_length=50)
    def __str__(self):
        return f'{self.nom}'

class FondantCremeux(models.Model):
    nom = models.fields.CharField(max_length=50)
    description = models.fields.TextField(max_length=200)
    couleur = models.fields.CharField(max_length=20)
    taille = models.fields.CharField(max_length=20)
    forme = models.fields.CharField(max_length=50)
    def __str__(self):
        return f'{self.nom}'

class Bruleurs(models.Model):
    nom = models.fields.CharField(max_length=50)
    description = models.fields.TextField(max_length=200)
    couleur = models.fields.CharField(max_length=20)
    taille = models.fields.CharField(max_length=20)
    forme = models.fields.CharField(max_length=50)
    def __str__(self):
        return f'{self.nom}'
