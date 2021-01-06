
from django.urls import path
from . import views
from rest_framework import generics
from .serializers import *

urlpatterns = [
    path('', views.index, name ='index'),

    path('Uzytkownik/', views.UzytkownikList.as_view()),
    path('Uzytkownik/<int:pk>/', views.UzytkownicyDetale.as_view()),

    path('Opcje_Biletu/', views.Opcje_BiletuList.as_view()),
    path('Opcje_Biletu/<int:pk>/', views.Opcje_BiletuDetale.as_view()),

    path('Podroze/', views.PodrozeList.as_view()),
    path('Podroze/<int:pk>/', views.PodrozeDetale.as_view()),

    path('Pociag/', views.PociagList.as_view()),
    path('Pociag/<int:pk>/', views.PociagDetale.as_view()),

    path('Wagon/', views.WagonList.as_view()),
    path('Wagon/<int:pk>/', views.WagonDetale.as_view()),

    path('Miejsce/', views.MiejsceList.as_view()),
    path('Miejsce/<int:pk>/', views.MiejsceDetale.as_view()),

    path('Bilet/', views.BiletList.as_view()),
    path('Bilet/<int:pk>/', views.BiletyDetale.as_view()),

    path('UzytkownikTworzy/', views.UzytkownikTworzy.as_view()),
    path('OpcjeBiletuTworzy/', views.Opcje_BiletuTworzy.as_view()),

    path('PodrozeTworzy/', views.PodrozeTworzy.as_view()),
    path('PociagTworzy/', views.PociagTworzy.as_view()),

    path('WagonTworzy/', views.WagonTworzy.as_view()),
    path('MiejsceTworzy/', views.MiejsceTworzy.as_view()),

    path('BiletTworzy/', views.BiletTworzy.as_view()),

]
