#!/usr/bin/env python3

import util

db = util.create_database()
for soup in util.soups_from_files("Documents/*.html"):
    for tag in soup.select('a[rel="bookmark"]'):
        name = tag.text
        if " " in name: continue
        path = "http:" + tag["href"]
        util.insert(db, name, path)
