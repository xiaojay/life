#coding=utf-8
import os,sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'life.settings'
import django
django.setup()
from django.conf import settings
settings.DEBUG = False
from taxonomy.models import *

data_dir = sys.argv[1]
gencode_file_name = 'gencode.dmp'
gencode_file = os.path.join(data_dir, gencode_file_name)
i = 0
for line in file(gencode_file):
    i = i + 1
    data = line.split('|')
    data = [d.strip() for d in data]
    GenCode.objects.create(genetic_code_id=data[0], abbreviation=data[1], 
                           name=data[2], cde=data[3], starts=data[4])
print 'Gencode: import %i data.'%i

division_file_name = 'division.dmp'
division_file = os.path.join(data_dir, division_file_name)
i = 0
for line in file(division_file):
    i = i + 1
    data = line.split('|')
    data = [d.strip() for d in data]
    Division.objects.create(division_id=data[0], division_code=data[1], division_name=data[2], comments=data[3])
print 'Division: import %i data.'%i

node_file_name = 'nodes.dmp'
node_file = os.path.join(data_dir, node_file_name)
i = 0
for line in file(node_file):
    i = i + 1
    data = line.split('|')
    data = [d.strip() for d in data]
    division = Division.objects.get(division_id=data[4])
    gencode = GenCode.objects.get(genetic_code_id=data[6])
    mitochondrial_gencode = GenCode.objects.get(genetic_code_id=data[8]) 
    
    if data[5] == '1':
        inherited_div_flag = True
    else:
        inherited_div_flag = False
    
    if data[7] == '1':
        inherited_gc_flag = True
    else:
        inherited_gc_flag = False
    
    if data[9] == '1':
        inherited_mgc_flag = True
    else:
        inherited_mgc_flag = False
    
    if data[10] == '1':
        genbank_hidden_flag = True
    else:
        genbank_hidden_flag = False
    
    if data[11] == '1':
        hidden_subtree_root_flag = True
    else:
        hidden_subtree_root_flag = False

    Node.objects.create(tax_id=data[0], rank=data[2], embl_code=data[3], division=division, 
                       inherited_div_flag=inherited_div_flag, genetic_code=gencode, inherited_gc_flag=inherited_gc_flag,
                       mitochondrial_genetic_code=mitochondrial_gencode, inherited_mgc_flag=inherited_mgc_flag,
                       genbank_hidden_flag=genbank_hidden_flag, hidden_subtree_root_flag=hidden_subtree_root_flag,
                       comments=data[12])
print 'Node: import %i data.'%i

for line in file(node_file):
    data = line.split('|')
    data = [d.strip() for d in data]
    if data[1]:
        node = Node.objects.get(tax_id=data[0])
        parent = Node.objects.get(tax_id=data[1])
        node.parent = parent
        node.save()
print 'Node:finished parent node import.'

delnodes_file_name = 'delnodes.dmp'
delnodes_file = os.path.join(data_dir, delnodes_file_name)
i = 0
for line in file(delnodes_file):
    i = i + 1
    data = line.split('|')
    data = [d.strip() for d in data]
    if data[0]:
        try:
            node = Node.objects.get(tax_id=data[0])
        except Node.DoesNotExist:
            print 'Node %s dosenot exist.'%data[0]
            continue
        node.deleted_flag = True
        node.save()
print 'Node:mark %i node deleted.'%i
