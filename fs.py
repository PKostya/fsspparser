from __future__ import absolute_import
import logging
import os
from random import randint
from copy import copy, deepcopy
import threading
import itertools
import collections
from six.moves.urllib.parse import urljoin
import email
from datetime import datetime
import weakref
import six

from weblib.html import find_refresh_url, find_base_url
from grab.document import Document
from grab import error
from weblib.http import normalize_http_values
from grab.cookie import CookieManager
from grab.proxylist import ProxyList, parse_proxy_line
from grab.deprecated import DeprecatedThings
from grab import Grab
import grab


__all__ = ('Grab', )

logger = logging.getLogger('grab.base')

logger_network = logging.getLogger('grab.network')

# Настройки объекта

g = Grab()
capUrl = 'http://is.fssprus.ru/ajax_search'
url = 'http://fssprus.ru/iss/ip/'
g.setup(
    log_file = 'fs_grab_log.txt',
    log_dir = '~/workspace/',
    debug_post = True,
    debug = True,
    verbose_logging = True,
    )


g.go(url, method = "POST")

if g.go(url, post = {
    'variant': '1',
    'last_name': 'Антон',
    'first_name': 'Петров'
    }):
    g1 = g.clone()
    print(g1.request_method)
else:
    print("Чет пошло не так")


if input(int()) == 1:
    g2 = g1.clone()