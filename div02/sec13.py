"""
13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
確認にはpasteコマンドを用いよ．
"""

with open("col1.txt") as f_col1, open("col2.txt") as f_col2, open("col1_and_col2.txt", "w") as f:
    for col1, col2 in zip(f_col1, f_col2):
        f.write(f"{col1.strip()}\t{col2.strip()}\n")
