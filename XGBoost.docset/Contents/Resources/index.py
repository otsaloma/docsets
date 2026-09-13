#!/usr/bin/env python3

import util

db = util.create_database()
for url, soup in util.pages():
    for tag in soup.select('dt.sig a.headerlink'):
        name = tag.attrs["href"].split("#")[-1]
        path = util.urljoin(url, tag.attrs["href"])
        util.insert(db, name, path)
