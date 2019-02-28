"""
25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
"""

import pprint
from div03.sec20 import get_wiki_text


def extract_basic_info(text):
    start = text.find("{{基礎情報")
    text = text[start:]

    # 入れ子の {{ }} を無視して、基礎情報テンプレート全体を取得する
    nest = 0
    for i in range(len(text)):
        t = text[i:i + 2]
        if t == "{{":
            nest += 1
        if t == "}}":
            nest -= 1
        if nest == 0:
            text = text[:i + 2]
            break

    # 入れ子の | を無視して、テンプレートのペアを取得する
    pairs = []
    start = 0
    nest1 = 0
    nest2 = 0
    for i in range(len(text)):
        if text[i] == "|":
            if start == 0:
                start = i + 1
            elif start != 0 and nest1 == 1 and nest2 == 0:
                pairs.append(text[start:i].strip())
                start = i + 1
        if text[i:i + 2] == "{{":
            nest1 += 1
        if text[i:i + 2] == "}}":
            nest1 -= 1
        if text[i:i + 1] == "[":
            nest2 += 1
        if text[i:i + 1] == "]":
            nest2 -= 1
    pairs.append(text[start:-2].strip())

    # 辞書化する
    result = {}
    for pair in pairs:
        separator = pair.find("=")
        result[pair[:separator].strip()] = pair[separator + 1:].strip()

    return result


if __name__ == "__main__":
    uk_text = get_wiki_text("イギリス")
    result_dict = extract_basic_info(uk_text)
    pprint.pprint(result_dict, width=1000)
