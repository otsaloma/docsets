#!/usr/bin/env python3

import util

db = util.create_database()
root = "https://dataiter.readthedocs.io/en/stable/"
for soup in util.soups_from_files("Documents/*.html"):
    for tag in soup.select('a[href*="#dataiter."]'):
        name = tag.attrs["href"].split("#")[-1]
        path = root + tag.attrs["href"]
        util.insert(db, name, path)
