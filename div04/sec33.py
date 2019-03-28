"""
33. サ変名詞
サ変接続の名詞をすべて抽出せよ．
"""

from div04.sec30 import get_neko_morphemes

morphemes_list = get_neko_morphemes()

result = []

for morphemes in morphemes_list:
    for morpheme in morphemes:
        if morpheme["pos"] == "名詞" and morpheme["pos1"] == "サ変接続":
            result.append(morpheme["surface"])

print(result[:10])
