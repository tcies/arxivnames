import urllib



for i in range(100):
  url = 'http://export.arxiv.org/api/query?search_query=all&start=%d&max_results=100' % (100 * i)
  data = urllib.urlopen(url).read()
  f = open('results/%03d.xml' % i, 'w')
  f.write(data)

