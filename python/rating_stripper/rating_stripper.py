#!/usr/bin/python

import sys
import re
import urllib

from bs4 import BeautifulSoup

SCORE_RE = re.compile(r'score(\d\d)')

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

#    for div in soup.find_all('div', attrs={'class', 'rating_profile'}):
#        print "%s,%s" % (div['data-title'], div['data-score'])
    for li in soup.find_all('li', attrs={'class', 'media_block'}):
        movie = li.find_next('a')['title']
        score = re.match(SCORE_RE,
                li.find('span',
                    attrs={'class': SCORE_RE})['class'][3]
                ).group(1)

        score = float(score) / 10

        print "%s,%s" % (movie, score)
