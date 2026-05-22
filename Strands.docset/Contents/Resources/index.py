#!/usr/bin/env python3

import util

from pathlib import Path

db = util.create_database()
for path in Path("Documents").glob("*.html"):
    url = util.url_from_filename(path)
    soup = util.soup_from_file(path)
    for tag in soup.select("a.sl-anchor-link"):
        name = tag.previous_sibling.text
        path = url + tag.attrs["href"]
        util.insert(db, name, path)
