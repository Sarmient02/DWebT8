from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('documentos/', views.documentos, name='documentos'),
    path('documentos/new/', views.new_document, name='new_document'),
    path('documentos/edit/<pk>', views.edit_document, name='edit_document'),
    path('documentos/delete/<pk>', views.delete_document, name='delete_document'),
    path('ciudades/', views.ciudades, name='ciudades'),
    path('ciudades/new/', views.new_ciudad, name='new_ciudad'),
    path('ciudades/edit/<pk>', views.edit_ciudad, name='edit_ciudad'),
    path('ciudades/delete/<pk>', views.delete_ciudad, name='delete_ciudad'),
    path('personas/', views.personas, name='personas'),
    path('personas/new/', views.new_persona, name='new_persona'),
    path('personas/edit/<pk>', views.edit_persona, name='edit_persona'),
    path('personas/delete/<pk>', views.delete_persona, name='delete_persona')
]