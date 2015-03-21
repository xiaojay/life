#coding=utf-8
from django.contrib import admin
from survey.models import *

class AlgaeAdmin(admin.ModelAdmin):
    list_display = ['name', 'chinese_name', 'phylum', 'biomass']
    list_filter = ['phylum',]

admin.site.register(Algae, AlgaeAdmin)
