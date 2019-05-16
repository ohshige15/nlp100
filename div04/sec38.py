"""
38. ヒストグラム
単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．
"""

from collections import Counter
import matplotlib.pyplot as plt
from div04.sec30 import get_neko_morphemes

morphemes_list = get_neko_morphemes()

words = Counter([morpheme["base"] for morphemes in morphemes_list for morpheme in morphemes]).most_common()
_, word_count = list(zip(*words))

plt.rcParams["font.family"] = "IPAexGothic"
plt.hist(word_count, bins=50, range=(1, 50))
plt.savefig("fig38.png")
