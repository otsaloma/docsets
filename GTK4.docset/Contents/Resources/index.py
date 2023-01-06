#!/usr/bin/env python3

import util

from pathlib import Path

db = util.create_database()
for path in Path("Documents").glob("*.html"):
    url = util.url_from_filename(path)
    root = url.rsplit("/", 1)[0]
    type = url.split("/")[-1].split(".")[0]
    soup = util.soup_from_file(path)
    title = soup.select_one("title").text
    util.insert(db, title, url)
    if type in ["class", "iface", "struct"]:
        # e.g. https://docs.gtk.org/gtk4/class.Notebook.html
        # e.g. https://docs.gtk.org/gtk4/iface.Actionable.html
        # e.g. https://docs.gtk.org/gtk4/struct.PaperSize.html
        children = ["ctor", "func", "method", "property", "signal"]
        children = [f".links a.{x}" for x in children]
        for tag in soup.select(",".join(children)):
            name = f"{title}.{tag.text}"
            path = f"{root}/{tag.attrs['href']}"
            util.insert(db, name, path)
    if type in ["enum", "error", "flags"]:
        # e.g. https://docs.gtk.org/gtk4/enum.DirectionType.html
        # e.g. https://docs.gtk.org/gtk4/error.DialogError.html
        # e.g. https://docs.gtk.org/gtk4/flags.StateFlags.html
        for tag in soup.select(".enum-members td > a"):
            name = tag.select_one("code").text
            path = f"{url}{tag.attrs['href']}"
            util.insert(db, name, path)
