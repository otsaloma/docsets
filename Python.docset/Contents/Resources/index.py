#!/usr/bin/env python3

import util

db = util.create_database()
root = "https://docs.python.org/3/"
for soup in util.soups_from_files("Documents/*.html"):
    for tag in soup.select('a[href^="library/"]'):
        name = tag.attrs["href"].split("#")[-1]
        if name.startswith("cmdoption-"): continue
        if name.startswith("index-"): continue
        if name.startswith("opcode-"): continue
        name = name.replace("module-", "")
        path = root + tag.attrs["href"]
        util.insert(db, name, path)
