"""
26. 強調マークアップの除去
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．
"""

import re
from div03.sec20 import get_wiki_text
from div03.sec25 import extract_basic_info

bold_regex = re.compile(r"'''(.+?)'''")
italic_regex = re.compile(r"''(.+?)''")


def remove_emphasis(text):
    text = bold_regex.sub(r"\1", text)
    text = italic_regex.sub(r"\1", text)
    return text


if __name__ == "__main__":
    import pprint
    uk_text = get_wiki_text("イギリス")
    result_dict = extract_basic_info(uk_text)
    result_dict = {k: remove_emphasis(v) for k, v in result_dict.items()}
    pprint.pprint(result_dict, width=1000)
