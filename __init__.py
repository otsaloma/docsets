# -*- coding: utf-8 -*-

import atexit
import bs4
import glob
import os
import requests
import sqlite3

rs = requests.Session()

def create_database(fname="docSet.dsidx"):
    if os.path.isfile(fname):
        os.remove(fname)
    db = sqlite3.connect(fname)
    atexit.register(db.close)
    atexit.register(db.commit)
    cursor = db.cursor()
    cursor.execute("CREATE TABLE searchIndex(id INTEGER PRIMARY KEY, name TEXT, type TEXT, path TEXT);")
    cursor.execute("CREATE UNIQUE INDEX anchor ON searchIndex (name, type, path);")
    return db

def insert(db, name, type, path):
    print("{}: {}: {}".format(name, type, path))
    cursor = db.cursor()
    cursor.execute("INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?);", (name, type, path))

def soup_from_file(fname):
    print("Parsing {}".format(fname))
    page = open(fname, encoding="utf_8", errors="ignore").read()
    return bs4.BeautifulSoup(page, "html.parser")

def soup_from_url(url):
    print("Parsing {}".format(url))
    page = rs.get(url).text
    return bs4.BeautifulSoup(page, "html.parser")

def soups_from_files(pattern):
    return map(soup_from_file, glob.glob(pattern))
