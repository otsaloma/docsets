#!/usr/bin/env python3

import util

db = util.create_database()
for url, soup in util.pages():
    for tag in soup.select("a.sl-anchor-link"):
        name = tag.previous_sibling.text
        path = util.urljoin(url, tag.attrs["href"])
        util.insert(db, name, path)
