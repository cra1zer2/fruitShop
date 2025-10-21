from django.db import models
from django.utils import timezone

class Owoc(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.TextField()
    cena_za_kg = models.DecimalField(max_digits=10, decimal_places=2)
    kraj_pochodzenia = models.CharField(max_length=50)
    dostepna_ilosc = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nazwa

class Klient(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    numer_telefonu = models.CharField(max_length=15, blank=True)
    data_rejestracji = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"

class Zamowienia(models.Model):
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    owoc = models.ForeignKey(Owoc, on_delete=models.CASCADE)
    ilosc = models.IntegerField()
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.klient} {self.ilosc} {self.owoc}"
