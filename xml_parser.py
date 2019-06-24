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
   if len(entry['author']) > 1:
     authors = [i['name'] for i in entry['author']]
   else:
     authors = entry['author']['name']
   things.append(authors)

with open('authors.json', 'w') as fd:
   fd.write(json.dumps(things))
