#!/usr/bin/env python3

import util

db = util.create_database()
root = "https://developer.mozilla.org"
for soup in util.soups_from_files("Documents/*.html"):
    for tag in soup.select('.index a[href*="/en-US/docs/Web/CSS/"]'):
        name = tag.text
        if name[0].isupper(): continue
        path = root + tag.attrs["href"]
        util.insert(db, name, path)
