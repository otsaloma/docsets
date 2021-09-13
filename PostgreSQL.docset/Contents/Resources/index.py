#!/usr/bin/env python3

import util

db = util.create_database()
root = "https://www.postgresql.org/docs/current/static/"
for soup in util.soups_from_files("Documents/*.html"):
    for tag in soup.select('a[href^="queries-"], a[href^="sql-"]'):
        name = tag.text
        if not name.isupper(): continue
        path = root + tag.attrs["href"]
        util.insert(db, name, path)
