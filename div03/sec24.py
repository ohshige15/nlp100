"""
24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．
"""

import re
from div03.sec20 import get_wiki_text

text = get_wiki_text("イギリス")

for media in re.findall(r"\[\[(ファイル|File):(.+?)(\|.*)?\]\]", text):
    print(media[1])
