"""
23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
"""

import re
from div03.sec20 import get_wiki_text

text = get_wiki_text("イギリス")

section_reg = [
    (4, re.compile(r"=====(.+?)=====")),
    (3, re.compile(r"====(.+?)====")),
    (2, re.compile(r"===(.+?)===")),
    (1, re.compile(r"==(.+?)==")),
]

for line in text.split("\n"):
    line = line.strip()
    if not line.startswith("=="):
        continue
    for level, regex in section_reg:
        section = regex.match(line)
        if section is not None:
            print(section[1].strip(), level)
            break
