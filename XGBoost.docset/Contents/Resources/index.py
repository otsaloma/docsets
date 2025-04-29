#!/usr/bin/env python3

import util

db = util.create_database()
root = "https://xgboost.readthedocs.io/en/stable/python/python_api.html"
for soup in util.soups_from_files("Documents/*.html"):
    for tag in soup.select('dt.sig a.headerlink'):
        name = tag.attrs["href"].split("#")[-1]
        path = root + tag.attrs["href"]
        util.insert(db, name, path)
