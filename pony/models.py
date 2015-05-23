from django.db import models


class Journal_technicks (models.Model):
    typ = models.CharField(max_length=20)
    model = models.CharField(max_length=30)
    price = models.IntegerField()
    condition = models.BooleanField()
    availability = models.BooleanField()


class Journal_sdacha(models.Model):
    summa = models.IntegerField()
    ID_tec = models.IntegerField()
    fio = models.CharField(max_length=50)
    vzitie = models.TimeField()
    vozvr = models.TimeField()
    cdacha = models.BooleanField()
    opozd = models.TimeField()
    document = models.CharField(max_length=20)


class Journal_workers(models.Model):
    surname = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    fname = models.CharField(max_length=20)
    office = models.CharField(max_length=20)
