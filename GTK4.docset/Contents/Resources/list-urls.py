#!/usr/bin/env python3

import util

from pathlib import Path

urls = []
for root in [
    "https://docs.gtk.org/gdk-pixbuf/",
    "https://docs.gtk.org/gdk4/",
    "https://docs.gtk.org/gio/",
    "https://docs.gtk.org/glib/",
    "https://docs.gtk.org/gobject/",
    "https://docs.gtk.org/gtk4/",
    "https://docs.gtk.org/Pango/",
]:
    soup = util.soup_from_url(root)
    for a in soup.select("a.symbol"):
        urls.append(root + a.attrs["href"])
path = Path(__file__).with_name("URLS")
path.write_text("\n".join(urls) + "\n", "utf-8")
print(f"Wrote {len(urls)} URLs to {path.name}.")
