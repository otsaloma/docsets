#!/usr/bin/env python3

import re
import util

db = util.create_database()
root = "https://docs.djangoproject.com/en/3.2/"
for soup in util.soups_from_files("Documents/*.html"):
    for tag in soup.select(".index dt > a"):
        href = tag.attrs["href"]
        href = re.sub("^../", "", href)
        name = href.split("#")[-1]
        if not name.startswith("django."): continue
        path = root + href
        util.insert(db, name, path)
