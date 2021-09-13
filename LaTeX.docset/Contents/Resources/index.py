#!/usr/bin/env python3

import util

db = util.create_database()
root = "https://www.nic.funet.fi/pub/TeX/CTAN/info/latex2e-help-texinfo/latex2e.html"
for soup in util.soups_from_files("Documents/*.html"):
    for tag in soup.select('a[href*="#index-"]'):
        name = tag.text
        if not name.startswith("\\"): continue
        if not name[1].isalpha(): continue
        path = root + tag.attrs["href"]
        util.insert(db, name, path)
