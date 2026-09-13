#!/usr/bin/env python3

import util

db = util.create_database()
for url, soup in util.pages():
    for tag in soup.select('a[href^="queries-"], a[href^="sql-"]'):
        name = tag.text
        if not name.isupper(): continue
        path = util.urljoin(url, tag.attrs["href"])
        util.insert(db, name, path)
