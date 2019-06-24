import xmltodict

with open('results.xml') as fd:
    doc = xmltodict.parse(fd.read())

print doc['feed']
