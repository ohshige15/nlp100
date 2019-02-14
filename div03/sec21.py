"""
21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．
"""

from div03.sec20 import get_wiki_text

text = get_wiki_text("イギリス")

for line in text.split("\n"):
    if line.startswith("[[Category:"):
        print(line.strip())
