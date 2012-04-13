#!/usr/bin/python

import sys
import re
import urllib

from bs4 import BeautifulSoup

SCORE_RE = re.compile(r'score(\d\d)')

LINK = \
"https://www.rottentomatoes.com/user/id/%s/ratings?profileUserId=%s&sortby=" \
"ratingDate&pageNum=" \
% (783076641, 783076641)

first_movie = None
i = 0

while True:
    i += 1
    url = '%s%s' % (LINK, i)
    print >>sys.stderr, "opening %s" % url
    html = urllib.urlopen(url).read()
    clean_html = re.sub(r'css""', r'css"', html, count=0)
    with open('url%s.html' % i, 'w') as f:
        print >>f, html

# Remove stupid "" from line 321

    soup = BeautifulSoup(clean_html)

    n_movies = 0

#    for div in soup.find_all('div', attrs={'class', 'rating_profile'}):
#        print "%s,%s" % (div['data-title'], div['data-score'])
    for li in soup.find_all('li', attrs={'class', 'media_block'}):
        movie = li.find_next('a')['title']
        score = re.match(SCORE_RE,
                li.find('span',
                    attrs={'class': SCORE_RE})['class'][3]
                ).group(1)

        score = float(score) / 10

        if i == 1 and n_movies == 0:
            first_movie = movie
        elif movie == first_movie:
            break

        print u"%s,%s" % (movie, score)

        n_movies += 1

    if n_movies < 10:
        break
