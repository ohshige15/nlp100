"""
36. 単語の出現頻度
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
"""

from collections import Counter
from div04.sec30 import get_neko_morphemes

morphemes_list = get_neko_morphemes()

words = Counter([morpheme["base"] for morphemes in morphemes_list for morpheme in morphemes]).most_common()
print(words[:10])
