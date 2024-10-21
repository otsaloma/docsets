#!/usr/bin/env python3

import util

db = util.create_database()
for soup in util.soups_from_files("Documents/*.html"):
    link = soup.select_one('link[rel="canonical"]')
    root = link.attrs["href"]
    for tag in soup.select('.doc-heading a.headerlink'):
        name = tag.attrs["href"].split("#")[-1]
        path = root + tag.attrs["href"]
        util.insert(db, name, path)
