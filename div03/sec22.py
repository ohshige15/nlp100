"""
22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
"""

import re
from div03.sec20 import get_wiki_text

text = get_wiki_text("イギリス")

category_reg = re.compile(r"\[\[Category:(.*?)(\|.*?)?\]\]")

for line in text.split("\n"):
    category = category_reg.match(line.strip())
    if category is not None:
        print(category[1])
