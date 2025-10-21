from django.urls import path
from . import views

app_name = 'shop_app'

urlpatterns = [
    path('owoce/', views.lista_owocow, name='lista_owocow'),
    path('klienci/', views.lista_klientow, name='lista_klientow'),
    path('zamowienia/', views.lista_zamowien, name='zamowienia'),

]