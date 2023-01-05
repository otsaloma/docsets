#!/usr/bin/env python3

import util

db = util.create_database()
root = "https://requests.readthedocs.io/en/latest/api/"
for soup in util.soups_from_files("Documents/*.html"):
    for tag in soup.select('dt[id^="requests."]'):
        name = tag.attrs["id"]
        path = "#".join((root, name))
        util.insert(db, name, path)
