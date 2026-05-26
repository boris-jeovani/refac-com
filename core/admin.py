from django.contrib import admin

from .models import (
    Contact,
    Projet,
    Galerie,
    Partenaire,
    Actualite,
    Newsletter
)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = (
        'nom',
        'email',
        'sujet',
        'date_envoi'
    )

    search_fields = (
        'nom',
        'email',
        'sujet'
    )

    list_filter = (
        'date_envoi',
    )


@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):

    list_display = ('titre',)


@admin.register(Galerie)
class GalerieAdmin(admin.ModelAdmin):

    list_display = ('titre',)


@admin.register(Partenaire)
class PartenaireAdmin(admin.ModelAdmin):

    list_display = ('nom',)

@admin.register(Actualite)
class ActualiteAdmin(admin.ModelAdmin):

    list_display = (
        'titre',
        'date_publication'
    )

    search_fields = (
        'titre',
        'contenu'
    )

    list_filter = (
        'date_publication',
    )

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):

    list_display = (
        'email',
        'date_abonnement'
    )

    search_fields = (
        'email',
    )

    list_filter = (
        'date_abonnement',
    )