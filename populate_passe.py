#!/usr/bin/env python
import os
import sys
import django
import re

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "passefeed.settings")
django.setup()

from pdb_store import models
from pdb_store.models import *

from bs4 import BeautifulSoup, NavigableString
import glob
path = "../pdbs/dorothy_wordsworth/OEBPS/*.html"
diary = []

def LETTER_paragraph_letters(items_soup):
  letters = []
  letter = []
  ps = items_soup.findAll('p');
  for p in ps:
    if re.search('LETT', p.get_text()):
      letters.append(letter) 
      letter = []
    letter.append(p.get_text())
  return letters

def classed_paragraph_letters(items_soup):
  letters = []
  letter = []
  ps = items_soup.findAll('p');
  for p in ps:
    if p.get('class'):
      letters.append(letter) 
      letter = []
    letter.append(p.get_text())
  return letters

def styled_paragraph_letters(items_soup):
  letters = []
  letter = []
  ps = items_soup.findAll('p');
  for p in ps:
    if p.attrs.get('style'):
      letters.append(letter) 
      letter = []
    letter.append(p.get_text())
  return letters

def paragraph_letters(items_soup):
  letters = []
  letter = []
  ps = items_soup.findAll('p');
  for p in ps:
    content = p.get_text()
    if re.search('utenberg', content) or re.search('F.', content):
      continue
    letters.append([content])
  return letters


def simple_paragraph_letters(items_soup):
  diary = []
  ps = items_soup.findAll('p');
  for p in ps:
    print(p)
    content = p.get_text()
    if content and content[0].isdigit() and content[1] != '.':
      diary.append(content) 
  return diary

def create_diary_item(diary, a):
  for d in diary:
    db_fi = FeedItem.objects.create(author=a)
    db_fi_part = Part.objects.create(feed_item=db_fi, part=d)

def create_letter_item(letters, a):
  for l in letters:
    if len(l) < 3:
      print(l)
      continue
    if len(l) > 10:
      print(l)
      continue
    if len(l[0]) < 20:
      continue
    if len(l[2]) < 200:
      continue
    db_l = FeedItem.objects.create(author=a)
    for p in l:
      db_p = Part.objects.create(part=p, feed_item=db_l)

def pgepubid_letters(items_soup):
  letters = []
  letter = []
  #letter_starts = items_soup.findAll('p', class_=lambda x: x and x.startswith('pgepubid')) 
  letter_starts = items_soup.findAll('p', class_=lambda x: x and (x == 'chead' or x == 'r')) 
  for letter_start in letter_starts:
    if letter_start:
      if letter_start.get('class') == 'r' and not letter_start.find('span'):
        continue
      letters.append(letter)
      letter = [ letter_start.get_text() ]
      for s in letter_start.next_siblings:
        if isinstance(s, NavigableString):
          continue
        if s.get('class'):
          #if re.match('chead', s.get('id')) and s.name == 'p':
          if 'chead' == s.get('class') and s.name == 'p':
            break
        text = s.get_text()
        if not text or not re.search('[A-Za-z]+', text) or text == 'List of Letters':
          continue
        letter.append(text)
      else:
       continue
  return letters

letters = []
for filename in glob.glob(path):
  output = ''
  with open(filename,'r') as f:
    output = f.read()
  items_soup = BeautifulSoup(output, features="html.parser")
  letters.extend(paragraph_letters(items_soup))
      
print(len(letters))

a, created = Author.objects.get_or_create(name='Dorothy Wordsworth')

for l in letters:
  #print(len(l))
  if not len(l):
    continue
#  if len(l) == 1:
#    continue
  if len(l[0]) < 300:
    continue
  print('---------------------')
  print(l)
#  print(l)
  db_l = FeedItem.objects.create(author=a)
  for p in l:
    db_p = Part.objects.get_or_create(part=p, feed_item=db_l)
