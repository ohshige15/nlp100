"""
27. 内部リンクの除去
26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．
"""

import re
from div03.sec20 import get_wiki_text
from div03.sec25 import extract_basic_info
from div03.sec26 import remove_emphasis

internal_link_with_text_regex = re.compile(r"\[\[[^\[\]\|\:]+?\|([^\[\]\|\:]+?)\]\]")
internal_link_without_text_regex = re.compile(r"\[\[([^\[\]\|\:]+?)\]\]")


def remove_internal_link(text):
    text = internal_link_with_text_regex.sub(r"\1", text)
    text = internal_link_without_text_regex.sub(r"\1", text)
    return text


def _remove(text):
    text = remove_emphasis(text)
    text = remove_internal_link(text)
    return text


if __name__ == "__main__":
    import pprint
    uk_text = get_wiki_text("イギリス")
    result_dict = extract_basic_info(uk_text)
    result_dict = {k: _remove(v) for k, v in result_dict.items()}
    pprint.pprint(result_dict, width=1000)
