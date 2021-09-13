#!/usr/bin/env python3

import util

db = util.create_database()
root = "https://www.gnu.org/software/emacs/manual/html_node/elisp/"
for soup in util.soups_from_files("Documents/*.html"):
    for tag in soup.select('a[href*="#index-"]'):
        name = tag.text
        if " " in name: continue
        if not name[0].isalpha(): continue
        path = root + tag.attrs["href"]
        util.insert(db, name, path)
