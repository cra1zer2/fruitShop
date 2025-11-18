from django.urls import path
from . import views

urlpatterns = [
    path('klienci/', views.lista_klientow_view, name='lista_klientow'),
    path('owoce/', views.lista_owocow_view, name='lista_owocow'),
    path('zamowienia/', views.lista_zamowien_view, name='lista_zamowien'),
]