from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('new_search', views.new_search, name='new_search'),
]