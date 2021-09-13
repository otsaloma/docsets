#!/usr/bin/env python3

import util

db = util.create_database()
root = "https://www.gnu.org/software/bash/manual/html_node/"
for soup in util.soups_from_files("Documents/*.html"):
    for tag in soup.select('a[href*="#index-"]'):
        name = tag.text
        path = root + tag.attrs["href"]
        util.insert(db, name, path)
