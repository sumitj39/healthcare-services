from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Service(models.Model):
    sname = models.CharField(max_length=50)
    desc = models.CharField(max_length=75)
    unit_price = models.IntegerField()

    def __unicode__(self):
        return self.sname

class Disease(models.Model):
    dname = models.CharField(max_length=50)
    d_desc = models.CharField(max_length=100)
    symptoms = models.CharField(max_length=100)

    def __unicode__(self):
        return self.dname

class DiseaseService(models.Model):
    dservice=models.ForeignKey(to=Service,on_delete=models.CASCADE)
    sdisease = models.ForeignKey(to=Disease,on_delete=models.CASCADE)

    def __unicode__(self):
        return self.dservice+" "+self.sdisease

    class Meta:
        unique_together = (('dservice','sdisease'),)

class Location(models.Model):
    lname = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=6)
    costofliving = models.FloatField()

    def __unicode__(self):
        return self.lname

class Hospital(models.Model):
    hname = models.CharField(max_length=50)
    points = models.IntegerField() # ratings for hospital
    hlocation = models.ForeignKey(to=Location,on_delete=models.CASCADE)

    def __unicode__(self):
        return self.hname

class Specialization(models.Model):
    hosp = models.ForeignKey(to=Hospital,on_delete=models.CASCADE)
    disease_service = models.ForeignKey(to=DiseaseService,on_delete=models.CASCADE)
    rate = models.FloatField()

    def __unicode__(self):
        return  self.hosp+' '+self.disease_service

    class Meta:
        unique_together = (('hosp','disease_service'),)

