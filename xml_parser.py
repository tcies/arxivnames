import IPython
# import ipdb; ipdb.set_trace()
import json
import xmltodict
from IPython.core import ultratb
import sys


sys.excepthook = ultratb.FormattedTB(
color_scheme='Linux', call_pdb=1)


with open('results.xml') as fd:
    doc = xmltodict.parse(fd.read())

things = []  
for entry in doc['feed']['entry']:
   if 'name' in entry['author']:
     authors = entry['author']['name']
   else:
     authors = [i['name'] for i in entry['author']]
   things.append(authors)

with open('authors.json', 'w') as fd:
   fd.write(json.dumps(things))

f = open('authors.txt', 'w')
for au in things:
    if type(au) == unicode:
        au = [au]
    for aaa in au:
        f.write('%s, ' % aaa.encode('utf-8'))
    f.write('\n')

# Column thingy
f = open('oneauth.csv', 'w')
fi = open('indices.txt', 'w')
for index, authors in enumerate(things):
    if type(authors) == unicode:
        authors = [authors]
    initials = False
    for author in authors:
        if author[1] == '.':
            initials = True
    if initials:
        continue
    for author in authors:
        names = author.split(' ')
        f.write('%s\n' % names[0].encode('utf-8'))
        fi.write('%d\n' % index)

# IPython.embed()
