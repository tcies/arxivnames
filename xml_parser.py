import IPython
# import ipdb; ipdb.set_trace()
import json
import xmltodict
from IPython.core import ultratb
import sys


sys.excepthook = ultratb.FormattedTB(
color_scheme='Linux', call_pdb=1)



things = []  


for i in range(100):
  with open('results/%03d.xml' % i) as fd:
      doc = xmltodict.parse(fd.read())

  if 'entry' not in doc['feed']:
    continue

  for entry in doc['feed']['entry']:
     if 'name' in entry['author']:
       authors = entry['author']['name']
     else:
       authors = [i['name'] for i in entry['author']]
     things.append(authors)

# Column thingy
f = open('oneauth.csv', 'w')
fi = open('indices.txt', 'w')
for index, authors in enumerate(things):
    if type(authors) == unicode:
        authors = [authors]
    initials = False
    for author in authors:
        if len(author) < 2 or author[1] == '.':
            initials = True
    if initials:
        continue
    for author in authors:
        names = author.split(' ')
        f.write('%s\n' % names[0].encode('utf-8'))
        fi.write('%d\n' % index)

IPython.embed()
