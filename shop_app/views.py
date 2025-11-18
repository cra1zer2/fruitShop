from django.shortcuts import render
from .models import Klient, Owoc, Zamowienia

def strona_glowna(request):
    return render(request, 'base.html')

def lista_klientow_view(request):
    klienci = Klient.objects.all()
    return render(request, 'lista_klientow.html', {'klienci': klienci})

def lista_owocow_view(request):
    owoce = Owoc.objects.all()
    return render(request, 'lista_owocow.html', {'owoce': owoce})

def lista_zamowien_view(request):
    zamowienia = Zamowienia.objects.all()
    return render(request, 'lista_zamowien.html', {'zamowienia': zamowienia})