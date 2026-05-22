#!/usr/bin/env python3

import re
import util

from pathlib import Path

urls = []
for line in util.lines_from_url("https://strandsagents.com/llms.txt"):
    if match := re.search(r"https://strandsagents.com/docs/api/python/.*?/index.md", line):
        urls.append(match.group(0).replace("index.md", "index.html"))

path = Path(__file__).with_name("URLS")
path.write_text("\n".join(urls) + "\n", "utf-8")
print(f"Wrote {len(urls)} URLs to {path.name}.")
