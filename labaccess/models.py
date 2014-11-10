from django.db import models
#from datetime import datetime


class Verantwortlicher(models.Model):
    verantwortlicher_text = models.CharField("Nachname", max_length=200)
    firstname_text = models.CharField("Vorname", max_length=200, blank=True)
    titel_text = models.CharField("Titel", max_length=200, blank=True)

    def __str__(self):
        return self.verantwortlicher_text


class Labor(models.Model):
    verantwortlicher = models.ForeignKey(Verantwortlicher)
    labor_text = models.CharField("Labor", max_length=200)
    laborname = models.CharField("Laborname", max_length=200, blank=True)

    def __str__(self):
        return self.labor_text


class Zugang(models.Model):
    zugang_v = models.ForeignKey(Verantwortlicher)
    zugang_l = models.ForeignKey(Labor)
    zugang_vname = models.CharField("Vorname", max_length=50)
    zugang_nname = models.CharField("Nachname", max_length=50)
    zugang_matnr = models.CharField("Matrikelnummer", max_length=5)
    zugang_email = models.EmailField(max_length=254)
    zugang_begruendung = models.CharField("Begründung", max_length=200)
    zugang_semester = models.CharField("Semester", max_length=2)
    zugang_anfrage_date = models.DateTimeField("Zugangsanfragen Datum")
    zugang_genehmigt_date = models.DateTimeField("Genehmigung Datum", null=True)

    def __str__(self):
        return self.zugang_v.verantwortlicher_text