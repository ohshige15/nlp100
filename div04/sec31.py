"""
31. 動詞
動詞の表層形をすべて抽出せよ．
"""

from div04.sec30 import get_neko_morphemes

morphemes_list = get_neko_morphemes()

result = []

for morphemes in morphemes_list:
    for morpheme in morphemes:
        if morpheme["pos"] == "動詞":
            result.append(morpheme["surface"])

print(result[:10])
