from django.db import models


class Contact(models.Model):

    nom = models.CharField(max_length=100)

    email = models.EmailField()

    sujet = models.CharField(max_length=200)

    message = models.TextField()

    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom


class Projet(models.Model):

    titre = models.CharField(max_length=200)

    description = models.TextField()

    image = models.ImageField(
        upload_to='projects/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.titre


class Galerie(models.Model):

    titre = models.CharField(max_length=200)

    image = models.ImageField(
        upload_to='galerie/'
    )

    def __str__(self):
        return self.titre
    
class Partenaire(models.Model):

    nom = models.CharField(max_length=200)

    logo = models.ImageField(
        upload_to='partenaires/'
    )

    def __str__(self):
        return self.nom
    
class Actualite(models.Model):

    titre = models.CharField(max_length=250)

    contenu = models.TextField()

    image = models.ImageField(
        upload_to='actualites/',
        blank=True,
        null=True
    )

    date_publication = models.DateTimeField(
        auto_now_add=True
    )
    slug = models.SlugField(
    unique=True,
    blank=True
)

    def __str__(self):

        return self.titre
    
class Newsletter(models.Model):

    email = models.EmailField(
        unique=True
    )

    date_abonnement = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.email