from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('documentos/', views.documentos, name='documentos'),
    path('documentos/new/', views.new_document, name='new_document'),
    path('documentos/edit/<pk>', views.edit_document, name='edit_document'),
    path('documentos/delete/<pk>', views.delete_document, name='delete_document')
]