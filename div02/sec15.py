"""
15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
"""

N = int(input())
with open("hightemp.txt") as f:
    result = f.readlines()[-N:]
    print("\n".join([r.strip() for r in result]))
