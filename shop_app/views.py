from django.shortcuts import render
from .models import Owoc, Klient, Zamowienia

def lista_owocow(request):
    owoce = Owoc.objects.all()

    return render(request, 'shop_app/lista_owocow.html', {'owoce': owoce})

def lista_klientow(request):
    klienci = Klient.objects.all()

    return render(request, 'shop_app/lista_klientow.html', {'klienci': klienci})

def lista_zamowien(request):
    zamowienia = Zamowienia.objects.all()
    return render(request, 'shop_app/lista_zamowien.html', {'zamowienia': zamowienia})
