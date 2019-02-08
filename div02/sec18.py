"""
18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
"""

with open("hightemp.txt") as f:
    lines = [line.strip().split() for line in f]
    lines.sort(key=lambda x: float(x[2]), reverse=True)
    print("\n".join(["\t".join(line) for line in lines]))
