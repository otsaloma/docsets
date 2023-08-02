#!/usr/bin/env python3

import util

db = util.create_database()
root = "https://docs.peewee-orm.com/en/latest/"
for soup in util.soups_from_files("Documents/*.html"):
    for tag in soup.select('a[href*="api.html#"]'):
        name = tag.attrs["href"].split("#")[-1]
        path = root + tag.attrs["href"]
        util.insert(db, name, path)
