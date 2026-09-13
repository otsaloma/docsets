#!/usr/bin/env python3

import util

db = util.create_database()
for url, soup in util.pages():
    for tag in soup.select(".index dt > a"):
        name = tag.attrs["href"].split("#")[-1]
        if not name.startswith("django."): continue
        path = util.urljoin(url, tag.attrs["href"])
        util.insert(db, name, path)
