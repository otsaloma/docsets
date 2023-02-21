#!/usr/bin/env python3

import util

db = util.create_database()
root = "https://scikit-learn.org/stable/modules/"
for soup in util.soups_from_files("Documents/*.html"):
    for tag in soup.select('a.reference.internal[href^="generated/"]'):
        # Skip citations, e.g. "[R396fc7d924b8-1]"
        if tag.text.startswith("["): continue
        name = tag.attrs["title"]
        path = root + tag.attrs["href"]
        util.insert(db, name, path)
