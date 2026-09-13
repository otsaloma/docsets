#!/usr/bin/env python3

import util

db = util.create_database()
for url, soup in util.pages():
    title = soup.select_one("title").text.strip().split()[0]
    for tag in soup.select(f'a[href*="/en-US/docs/Web/API/{title}/"]'):
        name = ".".join(tag.attrs["href"].split("/")[-2:])
        path = util.urljoin(url, tag.attrs["href"])
        util.insert(db, name, path)
