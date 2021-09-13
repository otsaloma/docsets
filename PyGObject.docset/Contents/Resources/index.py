#!/usr/bin/env python3

import util

db = util.create_database()
for soup in util.soups_from_files("Documents/*.html"):
    tag = soup.select_one('.shortcuts .wy-breadcrumbs a')
    module = tag.text.replace(" ", "-")
    root = f"https://lazka.github.io/pgi-docs/{module}/"
    for tag in soup.select('a.reference.internal'):
        if not "title" in tag.attrs: continue
        name = tag.attrs["title"]
        path = root + tag.attrs["href"]
        util.insert(db, name, path)
