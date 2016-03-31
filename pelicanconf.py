#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'bobolopolis'
SITENAME = u'bobolopolis'
#SITEURL = u'https://bobolopolis.com'
SITEURL = u''
SITESUBTITLE = u'The Blog of Bob'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('GitHub', 'https://github.com/bobolopolis'),
          ('YouTube', 'https://www.youtube.com/channel/UCvQcTrwXywbXy5dGTfCm9nw'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#THEME = "simple"
THEME = "themes/pelican-twitchy"
CC_LICENSE = "CC-BY-SA"

