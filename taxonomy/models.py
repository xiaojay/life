#coding=utf-8
from django.db import models

#ftp://ftp.ncbi.nih.gov/pub/taxonomy/taxdump_readme.txt
class Node(models.Model):
    tax_id = models.CharField(max_length=20, unique=True)
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True)
    rank = models.CharField(max_length=20, null=True, blank=True)
    embl_code = models.CharField(max_length=10, null=True, blank=True)
    division = models.ForeignKey('Division', null=True, blank=True)
    inherited_div_flag = models.BooleanField(default=False)
    genetic_code = models.ForeignKey('GenCode', related_name='nodes', null=True, blank=True)
    inherited_gc_flag = models.BooleanField(default=False)
    mitochondrial_genetic_code = models.ForeignKey('GenCode', related_name='mitochondrial_nodes', null=True, blank=True)
    inherited_mgc_flag = models.BooleanField(default=False)
    genbank_hidden_flag = models.BooleanField(default=False)
    hidden_subtree_root_flag = models.BooleanField(default=False)
    comments = models.CharField(max_length=200, null=True, blank=True)
    
    #delnodes.dmp
    deleted_flag = models.BooleanField(default=False) 
    
    def __unicode__(self):
        return 'node:' + self.tax_id 

class Name(models.Model):
    node = models.ForeignKey(Node)
    name = models.CharField(max_length=100)
    unique_name = models.CharField(max_length=100)
    name_class = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return self.name

class ChineseName(models.Model):
    node = models.ForeignKey(Node)
    name = models.CharField(max_length=100)
    unique_name = models.CharField(max_length=100)
    name_class = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return self.name

class Division(models.Model):
    division_id = models.CharField(max_length=100)
    division_code = models.CharField(max_length=20, null=True, blank=True)
    division_name = models.CharField(max_length=50, null=True, blank=True)
    comments = models.CharField(max_length=200, null=True, blank=True)
    
    def __unicode__(self):
        return self.division_name

class GenCode(models.Model):
    genetic_code_id  = models.CharField(max_length=100)
    abbreviation  = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    cde = models.CharField(max_length=100, null=True, blank=True)
    starts = models.CharField(max_length=100, null=True, blank=True)
    
    def __unicode__(self):
        return self.name

class DelNode(models.Model):
    tax_id = models.CharField(max_length=20, unique=True)
    
    def __unicode__(self):
        return self.tax_id

class MergedNode(models.Model):
    old_tax_id = models.CharField(max_length=20, unique=True)
    new_tax_id = models.CharField(max_length=20, unique=True)

    def __unicode__(self):
        return '%s -> %s'%(self.old_tax_id, new_tax_id)
 
class Citation(models.Model):
    cit_id = models.CharField(max_length=20, unique=True)
    cit_key = models.CharField(max_length=200, null=True, blank=True)
    pubmed_id = models.CharField(max_length=20, unique=True)
    medline_id = models.CharField(max_length=20, unique=True)
    url = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    
    taxes = models.ManyToManyField('Node')

    def __unicode__(self):
        return self.cit_id
