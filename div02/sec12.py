"""
12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
"""

with open("hightemp.txt") as f, open("col1.txt", "w") as f_col1, open("col2.txt", "w") as f_col2:
    for line in f:
        col1, col2, *_ = line.strip().split("\t")
        f_col1.write(col1 + "\n")
        f_col2.write(col2 + "\n")
