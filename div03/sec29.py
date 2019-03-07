"""
29. 国旗画像のURLを取得する
テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）
"""

import requests
from div03.sec20 import get_wiki_text
from div03.sec25 import extract_basic_info
from div03.sec28 import remove_all_markup

uk_text = get_wiki_text("イギリス")
result_dict = extract_basic_info(uk_text)
result_dict = {k: remove_all_markup(v) for k, v in result_dict.items()}

flag_image = result_dict["国旗画像"]

url = "https://www.mediawiki.org/w/api.php"
params = {
    "action": "query",
    "titles": "File:" + flag_image,
    "prop": "imageinfo",
    "iiprop": "url",
    "format": "json",
}

response = requests.get(url, params=params)

if response.status_code == 200:
    result = response.json()
    try:
        urls = result["query"]["pages"]["-1"]["imageinfo"]
        for url in urls:
            print(url["url"])
    except KeyError:
        print("nothing")
else:
    print("error", response.status_code)
