from django.db import models


class ContactForm(models.Model):
    thema = models.CharField(max_length=100)
    vorname = models.CharField(max_length=100)
    nachname = models.CharField(max_length=100)
    firma = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    betreff = models.CharField(max_length=100)
    nachricht = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class KaufenForm(models.Model):
    vorname = models.CharField(max_length=100, blank=True)
    nachname = models.CharField(max_length=100, blank=True)
    firma = models.CharField(max_length=100, blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    betreff = models.CharField(max_length=100, blank=True)
    strasse = models.CharField(max_length=100, blank=True)
    hausnummer = models.CharField(max_length=100, blank=True)
    plz = models.CharField(max_length=100, blank=True)
    ort = models.CharField(max_length=100, blank=True)
    nachricht = models.TextField(blank=True)
    vorname_l = models.CharField(max_length=100, blank=True)
    nachname_l = models.CharField(max_length=100, blank=True)
    firma_l = models.CharField(max_length=100, blank=True)
    telephone_l = models.CharField(max_length=20, blank=True)
    email_l = models.EmailField(blank=True)
    betreff_l = models.CharField(max_length=100, blank=True)
    strasse_l = models.CharField(max_length=100, blank=True)
    hausnummer_l = models.CharField(max_length=100, blank=True)
    plz_l = models.CharField(max_length=100, blank=True)
    ort_l = models.CharField(max_length=100, blank=True)
    nachricht_l = models.TextField(blank=True)
