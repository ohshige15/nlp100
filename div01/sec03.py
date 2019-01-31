"""
03. 円周率
"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，
各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
"""

import string

text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
print(string.ascii_letters)
for word in text.split(" "):
    num_alpha = len([w for w in word if w in string.ascii_letters])
    print(num_alpha)
