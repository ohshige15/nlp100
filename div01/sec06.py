"""
06. 集合
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
"""

from div01.sec05 import generate_n_gram

string_x = "paraparaparadise"
string_y = "paragraph"

set_x = set(generate_n_gram(string_x, 2))
set_y = set(generate_n_gram(string_y, 2))

print(set_x.union(set_y))
print(set_x.intersection(set_y))
print(set_x.difference(set_y))

target = "se"
print(target in set_x)
print(target in set_y)
