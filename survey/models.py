#coding=utf-8
from django.db import models

class Algae(models.Model):
    name = models.CharField(max_length=100)
    chinese_name = models.CharField(max_length=100)
    phylum = models.CharField(max_length=100)
    biomass = models.FloatField(blank=True, null=True)

    def __unicode__(self):
        return '%s(%s)'%(self.chinese_name,self.name)


