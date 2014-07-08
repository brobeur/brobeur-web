# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Adds images in imgs folder into index.html 

# <markdowncell>

# Make a static blog site out of all the ipython notebook repos on github.com/wcmckee. Saves notebooks as rst and then converts the files to static blog. 
# Get Nikola working
# Test centos7

# <codecell>

ls

# <codecell>

import bs4

# <codecell>

lizim = 

# <codecell>

import os
import dominate 

# <codecell>

lisim = os.listdir('/home/pi/brobeur-web/imgs')

# <codecell>

lisim

# <codecell>

filwan = []

# <codecell>

dig cean ba4c053b67db73f90a2eff2fabcddb5f13812689334d8ea87d8b9e4d5e50e0fb

# <codecell>

for im in lisim:
    if 'png' or 'jpg' in im:
        filwan.append(im)

# <codecell>

filwan

# <codecell>

import dominate
from dominate.tags import *

doc = dominate.document(title='BroBeur Jam 2014')

with doc.head:
    link(rel='stylesheet', href='style.css')
    script(type='text/javascript', src='script.js')

with doc:
    with div(id='header').add(ol()):
        for i in filwan:
            (img(a(i.title)(), src='imgs/%s' % i))

    with div():
        attr(cls='body')
        p('Lorem ipsum..')

print doc

# <codecell>

import bs2

# <codecell>

opind = open('/home/pi/brobeur-web/index.html', 'r')

# <codecell>

opind.read()

# <codecell>


