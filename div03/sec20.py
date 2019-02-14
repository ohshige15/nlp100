"""
20. JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．
"""

import json


def get_wiki_text(title):
    with open("jawiki-country.json") as f:
        for line in f:
            wiki = json.loads(line)
            if wiki["title"] == title:
                return wiki["text"]
        return ""


if __name__ == "__main__":
    print(get_wiki_text("イギリス"))
