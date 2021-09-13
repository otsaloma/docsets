#!/usr/bin/env python3

import util

db = util.create_database()
root = "https://flask.palletsprojects.com/en/2.0.x/api/"
for soup in util.soups_from_files("Documents/*.html"):
    for tag in soup.select('dt[id^="flask."]'):
        name = tag.attrs["id"]
        path = "#".join((root, name))
        util.insert(db, name, path)
