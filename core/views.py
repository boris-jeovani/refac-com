from django.shortcuts import render

from django.core.paginator import Paginator

from django.db.models import Q

from django.shortcuts import get_object_or_404

from .models import (
    Contact,
    Projet,
    Galerie,
    Partenaire,
    Actualite,
    Newsletter
)

def home(request):

    partenaires = Partenaire.objects.all()

    success_newsletter = False

    erreur_newsletter = False

    if request.method == 'POST':

        email = request.POST.get('email')

        if email:

            Newsletter.objects.get_or_create(
                email=email
            )

            success_newsletter = True

        else:

            erreur_newsletter = True

    return render(
        request,
        'core/home.html',
        {
            'partenaires': partenaires,
            'success_newsletter': success_newsletter,
            'erreur_newsletter': erreur_newsletter
        }
    )

def about(request):
    return render(request, 'core/about.html')


def activities(request):
    return render(request, 'core/activities.html')

def projects(request):

    projets = Projet.objects.all()

    return render(request, 'core/projects.html', {

        'projets': projets

    })

def gallery(request):

    images = Galerie.objects.all()

    return render(request, 'core/gallery.html', {
        'images': images
    })

def contact(request):

    success = False

    if request.method == 'POST':

        nom = request.POST.get('nom')

        email = request.POST.get('email')

        sujet = request.POST.get('sujet')

        message = request.POST.get('message')

        Contact.objects.create(
            nom=nom,
            email=email,
            sujet=sujet,
            message=message
        )

        success = True

    return render(request, 'core/contact.html', {
        'success': success
    })

def actualites(request):

    recherche = request.GET.get('recherche')

    liste_actualites = Actualite.objects.order_by(
        '-date_publication'
    )

    if recherche:

        liste_actualites = liste_actualites.filter(

            Q(titre__icontains=recherche) |

            Q(contenu__icontains=recherche)

        )

    paginator = Paginator(
        liste_actualites,
        3
    )

    page_number = request.GET.get('page')

    actualites = paginator.get_page(
        page_number
    )

    return render(
        request,
        'core/actualites.html',
        {
            'actualites': actualites,
            'recherche': recherche
        }
    )

def detail_actualite(request, slug):

    actualite = get_object_or_404(
        Actualite,
        slug=slug
    )

    return render(
        request,
        'core/detail_actualite.html',
        {
            'actualite': actualite
        }
    )