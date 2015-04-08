#!/usr/bin/env python3
import bs4, os, re, sqlite3
os.chdir(os.path.dirname(__file__))
if os.path.isfile("docSet.dsidx"):
    os.remove("docSet.dsidx")
db = sqlite3.connect("docSet.dsidx")
cursor = db.cursor()
cursor.execute("CREATE TABLE searchIndex(id INTEGER PRIMARY KEY, name TEXT, type TEXT, path TEXT);")
cursor.execute("CREATE UNIQUE INDEX anchor ON searchIndex (name, type, path);")
root = "https://developer.gnome.org/gtk3/stable/"
for fname in ("api-index-full.html",):
    path = os.path.join("Documents", fname)
    page = open(path, encoding="utf_8", errors="ignore").read()
    soup = bs4.BeautifulSoup(page)
    for tag in soup.find_all("a", {"href": re.compile("^[^/]+#[^/]+$")}):
        name = tag.text.strip()
        if not name: continue
        path = root + tag.attrs["href"].strip()
        if path.endswith("-struct"): continue
        print("{}: {}".format(name, path))
        cursor.execute("INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)",
                       (name, "func", path))

db.commit()
db.close()
