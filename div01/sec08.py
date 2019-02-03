"""
08. 暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
 - 英小文字ならば(219 - 文字コード)の文字に置換
 - その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""


def cipher(text):
    ciphered = ""
    for char in text:
        if char.islower():
            ciphered += chr(219 - ord(char))
            continue
        ciphered += char

    return ciphered


if __name__ == "__main__":
    text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    print(cipher(text))
    print(cipher(cipher(text)))
