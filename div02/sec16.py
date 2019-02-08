"""
16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
"""

N = int(input())
with open("hightemp.txt") as f:
    lines = f.readlines()
    n = (len(lines) + N - 1) // N
    split_list = [lines[i * n:(i + 1) * n] for i in range(N)]
    print("\n".join(["".join(x) for x in split_list]))
