"""
19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
"""

from collections import Counter

with open("hightemp.txt") as f:
    lines = [line.strip().split()[0] for line in f]
    counter = Counter(lines)
    print(sorted(counter.items(), key=lambda x: x[1], reverse=True))
