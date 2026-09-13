#!/usr/bin/env python3

import util

db = util.create_database()
for url, soup in util.pages():
    for tag in soup.select('dt[id^="requests."]'):
        name = tag.attrs["id"]
        path = util.urljoin(url, "#" + name)
        util.insert(db, name, path)
