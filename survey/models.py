#coding=utf-8
from django.db import models

class Algae(models.Model):
    name = models.CharField(max_length=100)
    chinese_name = models.CharField(max_length=100)
    phylum = models.CharField(max_length=100)
    biomass = models.FloatField(blank=True, null=True)

    def __unicode__(self):
        return '%s(%s)'%(self.chinese_name,self.name)

class Survey(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True, null=True)
    start = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name

class Site(models.Model):
    survey = models.ForeignKey('Survey', )
    name = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100, blank=True, null=True)
    latitude =  models.CharField(max_length=100, blank=True, null=True)
    
    def __unicode__(self):
        return self.name
    
class Sample(models.Model):
    survey = models.ForeignKey('Survey')
    site = models.ForeignKey('Site')
    time = models.DateTimeField(blank=True, null=True)

class AlgaeData(models.Model):
    sample = models.ForeignKey('Sample')
    algae = models.ForeignKey('Algae')
    abundance = models.FloatField(blank=True, null=True)
    abundance_percent = models.FloatField(blank=True, null=True)
    biomass = models.FloatField(blank=True, null=True)
    biomass_percent = models.FloatField(blank=True, null=True)
