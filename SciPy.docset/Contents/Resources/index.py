#!/usr/bin/env python3

import util

db = util.create_database()
root = "https://docs.scipy.org/doc/scipy/reference/"
for soup in util.soups_from_files("Documents/*.html"):
    for tag in soup.select('a[href^="reference/generated/"]'):
        name = tag.attrs["href"].split("#")[-1]
        name = name.replace("module-", "")
        path = root + tag.attrs["href"]
        util.insert(db, name, path)
