"""
32. 動詞の原形
動詞の原形をすべて抽出せよ．
"""

from div04.sec30 import get_neko_morphemes

morphemes_list = get_neko_morphemes()

result = []

for morphemes in morphemes_list:
    for morpheme in morphemes:
        if morpheme["pos"] == "動詞":
            result.append(morpheme["base"])

print(result[:10])
