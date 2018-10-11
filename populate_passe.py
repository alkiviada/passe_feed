#!/usr/bin/env python
import os
import sys
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "passefeed.settings")
django.setup()

from pdb_store import models
from pdb_store.models import *

from bs4 import BeautifulSoup
import glob
path = "../pdbs/carlyle_to_emerson/OEBPS/*.html"
letters = []
letter = []
for filename in glob.glob(path):
  output = ''
  with open(filename,'r') as f:
    output = f.read()
  letters_soup = BeautifulSoup(output, features="html.parser")
  ps = letters_soup.findAll('p');
  for p in ps:
    if p.attrs.get('style'):
      letters.append(letter) 
      letter = []
    letter.append(p.get_text())

print(len(letters))
if not len(letters):
  exit

a = Author.objects.create(name='Carlyle')

for l in letters:
  if len(l) < 3:
    continue
  if len(l) > 10:
    continue
  if len(l[0]) < 20:
    continue
  if len(l[2]) < 200:
    continue
  db_l = Letter.objects.create(author=a)
  for p in l:
    db_p = Page.objects.create(page=p, letter=db_l)
  
