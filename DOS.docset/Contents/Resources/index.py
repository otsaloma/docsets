#!/usr/bin/env python3

import util

db = util.create_database()
root = "https://ss64.com/nt/"
for soup in util.soups_from_files("Documents/*.html"):
    for tag in soup.select('.az a[href$=".html"]'):
        name = tag.text
        path = root + tag.attrs["href"]
        util.insert(db, name, path)
