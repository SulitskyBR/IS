import random
import string


class VernamСipher:
    def __init__(self, key=None):
        initText = input("Введите открытый текст: ")
        self.P = initText
        self.len = len(initText)
        self.alf = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя" + string.ascii_lowercase + string.digits
        if key is None:
            self.K = self.key_create()
        else:
            self.K = key
        self.C = self.coder(self.P, self.K)

    def key_create(self):
        return "".join(random.choice(self.alf) for i in range(self.len))

    def coder(self, line, key):
        return "".join(chr(ord(c) ^ ord(k)) for c, k in zip(line, key))


def print_all(text):
    print("Текст:", text.P, "\nКлюч:", text.K, "\nШифротекст:", text.C)


def find_text(cypher, texts, s):
    possible_keys = []
    for f in range(len(texts)):
        for i in range(len(cypher[f]) - s + 1):
            key = [chr(ord(c) ^ ord(k)) for c, k in zip(cypher[f][i:i + s], texts[f])]
            intact_plaintext = text1.coder(cypher[f], key)
            if texts[f] in intact_plaintext:
                possible_keys.append(''.join(key))
    rez = [''.join(chr(ord(c) ^ ord(k)) for c, k in zip(t, possible_keys[-1])) for t in cypher]
    return rez

if __name__ == "__main__":
    text1 = VernamСipher()  # Первое слово
    text2 = VernamСipher(text1.K)  # Второе слово
    print_all(text1)
    print_all(text2)
    D = find_text([text1.C, text2.C], [text1.P, text2.P], text1.len)
    print("Декодированный текст 1:", D[0],
          "\nДекодированный текст 2:", D[1])
