#!/usr/bin/env python3

import util

db = util.create_database()
for url, soup in util.pages():
    for tag in soup.select('a[href*="api.html#"]'):
        name = tag.attrs["href"].split("#")[-1]
        path = util.urljoin(url, tag.attrs["href"])
        util.insert(db, name, path)
