#!/usr/bin/env python3
import bs4, glob, os, re, sqlite3
os.chdir(os.path.dirname(__file__))
if os.path.isfile("docSet.dsidx"):
    os.remove("docSet.dsidx")
db = sqlite3.connect("docSet.dsidx")
cursor = db.cursor()
cursor.execute("CREATE TABLE searchIndex(id INTEGER PRIMARY KEY, name TEXT, type TEXT, path TEXT);")
cursor.execute("CREATE UNIQUE INDEX anchor ON searchIndex (name, type, path);")
# Types.
for fname in glob.glob("Documents/sailfish-silica/sailfish-silica-all.html"):
    page = open(fname, encoding="utf_8", errors="ignore").read()
    soup = bs4.BeautifulSoup(page)
    for tag in soup.find_all("a", {"href": re.compile("qml-.*html")}):
        name = tag.text.strip()
        if not name: continue
        path = tag.attrs["href"].strip()
        path = "sailfish-silica/{}".format(path)
        print("{}: {}".format(name, path))
        cursor.execute("INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)",
                       (name, "func", path))

# Properties, signals and methods.
for fname in glob.glob("Documents/sailfish-silica/qml-*.html"):
    if fname.endswith("-members.html"): continue
    page = open(fname, encoding="utf_8", errors="ignore").read()
    soup = bs4.BeautifulSoup(page)
    title = soup.find_all("h1")[0].text.strip()
    for tag in soup.find_all("a", {"href": re.compile("-(prop|method|signal)")}):
        name = tag.text.strip()
        if not name: continue
        name = ".".join((title, name))
        path = tag.attrs["href"].strip()
        path = "sailfish-silica/{}".format(path)
        print("{}: {}".format(name, path))
        cursor.execute("INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)",
                       (name, "func", path))

db.commit()
db.close()
