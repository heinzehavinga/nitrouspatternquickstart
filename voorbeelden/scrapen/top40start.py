# Voorbeeldje hoe alle bolds uit Romeo en Juliet haalt
from pattern.web import URL, DOM
url = URL('http://www.top40.nl/top40/2016/week-37')
dom = DOM(url.download())
for song in dom('li[class="hitrecord"]'):
    print "een liedje!"
#  en nu hieronder per onderdeeltje de notering, aantal weken, artiest en titel
