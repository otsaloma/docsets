# -*- coding: utf-8 -*-

import atexit
import bs4
import functools
import glob
import hashlib
import requests
import sqlite3

from pathlib import Path

rs = requests.Session()

def create_database(fname="docSet.dsidx"):
    Path(fname).unlink(missing_ok=True)
    db = sqlite3.connect(fname)
    atexit.register(db.close)
    atexit.register(db.commit)
    cursor = db.cursor()
    cursor.execute("CREATE TABLE searchIndex(id INTEGER PRIMARY KEY, name TEXT, type TEXT, path TEXT);")
    cursor.execute("CREATE UNIQUE INDEX anchor ON searchIndex (name, type, path);")
    return db

def hash_urls(path):
    # Like in download.sh
    text = Path(path).read_text("utf-8")
    for url in filter(None, text.splitlines()):
        blob = (url.strip() + "\n").encode("utf-8")
        hash = hashlib.md5(blob).hexdigest()
        yield url, hash[:16]

@functools.cache
def hash_urls_reverse_map(path):
    return {hash: url for url, hash in hash_urls(path)}

def insert(db, name, path, type="func"):
    name = name.strip()
    path = path.strip()
    if not name or not path:
        return print(f"Ignoring ({name}, {path})")
    print(f"{name}: {path}")
    cursor = db.cursor()
    cursor.execute("INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?);", (name, type, path))

def soup_from_file(fname):
    print(f"Parsing {fname}...")
    text = Path(fname).read_text("utf-8")
    return bs4.BeautifulSoup(text, "html.parser")

def soup_from_url(url):
    print(f"Parsing {url}...")
    text = rs.get(url).text
    return bs4.BeautifulSoup(text, "html.parser")

def soups_from_files(pattern):
    return map(soup_from_file, glob.glob(pattern))

def url_from_filename(html_path):
    hash = Path(html_path).stem
    urls_path = Path(html_path).parent.parent / "URLS"
    return hash_urls_reverse_map(urls_path)[hash]
