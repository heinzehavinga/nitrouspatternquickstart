# Voorbeeldje hoe alle bolds uit Romeo en Juliet haalt
from pattern.web import URL, DOM
url = URL('http://shakespeare.mit.edu/romeo_juliet/full.html')
dom = DOM(url.download())
for bold in dom('b'):
  print bold[0]

#  draai dit programmatje af door "python bolds.py" te typen
#  als je "python bolds.py > lijst.csv" typt krijg je het als csv!