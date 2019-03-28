"""
35. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
"""

from div04.sec30 import get_neko_morphemes

morphemes_list = get_neko_morphemes()

result = []

for morphemes in morphemes_list:
    noun_list = []
    for morpheme in morphemes:
        if morpheme["pos"] == "名詞":
            noun_list.append(morpheme["surface"])
        else:
            if len(noun_list) > 1:
                result.append("".join(noun_list))
            noun_list = []
    else:
        if len(noun_list) > 1:
            result.append("".join(noun_list))

print(result[:10])
