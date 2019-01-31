"""
05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
"""


def generate_n_gram(sequence, n):
    return [sequence[i:i + n] for i in range(len(sequence) - n + 1)]


if __name__ == "__main__":
    text = "I am an NLPer"
    print(generate_n_gram(text, 2))
    print(generate_n_gram(text.split(" "), 2))
