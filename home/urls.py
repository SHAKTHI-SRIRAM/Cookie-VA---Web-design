from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('new_search', views.new_search, name='new_search'),
    path('google_search', views.google_search, name='google_search'),
    path('wiki_search', views.wiki_search, name='wiki_search'),
    path('ytube_search', views.ytube_search, name='ytube_search'),
    path('gmaps_search', views.gmaps_search, name='gmaps_search'),
    path('google_response', views.google_response, name='google_response'),
    path('wiki_response', views.wiki_response, name='wiki_response'),
    path('ytube_response', views.ytube_response, name='ytube_response'),
    path('gmaps_response', views.gmaps_response, name='gmaps_response'),
]