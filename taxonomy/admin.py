#coding=utf-8
from django.contrib import admin
from taxonomy.models import *

class NodeAdmin(admin.ModelAdmin):
    #list_display = ['genetic_code_id', 'abbreviation', 'name', 'cde', 'starts'] 
    #ordering = ['tax_id',]
    search_fields = ('tax_id', )

class GenCodeAdmin(admin.ModelAdmin):
    #list_display = ['genetic_code_id', 'abbreviation', 'name', 'cde', 'starts'] 
    ordering = ['genetic_code_id',]

class DivisionAdmin(admin.ModelAdmin):
    list_display = ['division_id', 'division_code', 'division_name', 'comments'] 
    ordering = ['division_id',]

admin.site.register(Node, NodeAdmin)
admin.site.register(GenCode, GenCodeAdmin)
admin.site.register(Division, DivisionAdmin)
