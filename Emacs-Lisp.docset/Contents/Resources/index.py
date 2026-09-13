#!/usr/bin/env python3

import util

db = util.create_database()
for url, soup in util.pages():
    for tag in soup.select('a[href*="#index-"]'):
        name = tag.text
        if " " in name: continue
        if not name[0].isalpha(): continue
        path = util.urljoin(url, tag.attrs["href"])
        util.insert(db, name, path)
