"""
14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
"""

N = int(input())
with open("hightemp.txt") as f:
    for _, line in zip(range(N), f):
        print(line.strip())
