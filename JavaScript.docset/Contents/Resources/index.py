#!/usr/bin/env python3

import util

db = util.create_database()
for url, soup in util.pages():
    for tag in soup.select('a[href*="/en-US/docs/Web/JavaScript/Reference/"]'):
        name = tag.text
        if not name: continue
        if " " in name: continue
        if not name[0].isalpha(): continue
        path = util.urljoin(url, tag.attrs["href"])
        util.insert(db, name, path)
