"""
10. 行数のカウント
行数をカウントせよ．確認にはwcコマンドを用いよ．
"""

with open("hightemp.txt") as f:
    n = 0
    for line in f:
        n += 1
    print(n)
