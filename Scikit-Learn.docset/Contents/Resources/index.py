#!/usr/bin/env python3

import util

db = util.create_database()
for url, soup in util.pages():
    for tag in soup.select('a.reference.internal[href^="generated/"]'):
        # Skip citations, e.g. "[R396fc7d924b8-1]"
        if tag.text.startswith("["): continue
        name = tag.attrs["title"]
        path = util.urljoin(url, tag.attrs["href"])
        util.insert(db, name, path)
