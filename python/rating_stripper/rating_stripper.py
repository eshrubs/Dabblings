#!/usr/bin/python

import sys
import re
import urllib

from bs4 import BeautifulSoup

LINK = \
"https://www.rottentomatoes.com/user/id/%s/ratings?profileUserId=%s&sortby=ratingDate&pageNum=" \
% (783076641, 783076641)

for i in range(1, 39):
    url = '%s%s' % (LINK, i)
    print >>sys.stderr, "opening %s" % url
    html = urllib.urlopen(url).read()
    clean_html = re.sub(r'css""', r'css"', html, count=0)
    with open('url%s.html' % i, 'w') as f:
        print >>f, html

# Remove stupid "" from line 321

    soup = BeautifulSoup(clean_html)

    for div in soup.find_all('div', attrs={'class', 'rating_profile'}):
        print "%s,%s" % (div['data-title'], div['data-score'])
