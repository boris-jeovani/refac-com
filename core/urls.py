from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('about/', views.about, name='about'),

    path('activities/', views.activities, name='activities'),

    path('projects/', views.projects, name='projects'),

    path('gallery/', views.gallery, name='gallery'),

      path(
    'actualites/',
    views.actualites,
    name='actualites'
),

path(
    'actualites/<slug:slug>/',
    views.detail_actualite,
    name='detail_actualite'
),

    path('contact/', views.contact, name='contact'),

  
]