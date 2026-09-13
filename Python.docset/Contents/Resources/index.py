#!/usr/bin/env python3

import util

db = util.create_database()
for url, soup in util.pages():
    for tag in soup.select('a[href^="library/"]'):
        name = tag.attrs["href"].split("#")[-1]
        if name.startswith("cmdoption-"): continue
        if name.startswith("index-"): continue
        if name.startswith("opcode-"): continue
        name = name.replace("module-", "")
        path = util.urljoin(url, tag.attrs["href"])
        util.insert(db, name, path)
