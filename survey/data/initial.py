#coding=utf-8
import os,sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'life.settings'
import django
django.setup()
from django.conf import settings
settings.DEBUG = False
from survey.models import *

Algae.objects.all().delete()
fn = 'Algae.txt'
lines = open(fn).readlines()
for line in lines[1:]:
    data = line.strip().split()
    a = Algae(name=data[2], chinese_name=data[1].decode('u8'),\
              phylum=data[0].decode('u8'))
    if len(data) == 4:
        a.biomass = data[3]
    a.save()

