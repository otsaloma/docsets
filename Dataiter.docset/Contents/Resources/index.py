#!/usr/bin/env python3

import util

db = util.create_database()
root = "https://dataiter.readthedocs.io/en/latest/"
for soup in util.soups_from_files("Documents/*.html"):
    for tag in soup.select('a[href*="#dataiter."]'):
        name = tag.attrs["href"].split("#")[-1]
        path = root + name
        util.insert(db, name, path)
