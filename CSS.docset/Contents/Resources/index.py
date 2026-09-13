#!/usr/bin/env python3

import util

db = util.create_database()
for url, soup in util.pages():
    for tag in soup.select('.index a[href*="/en-US/docs/Web/CSS/"]'):
        name = tag.text
        if name[0].isupper(): continue
        path = util.urljoin(url, tag.attrs["href"])
        util.insert(db, name, path)
