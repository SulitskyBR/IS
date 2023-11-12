
import random
import string

class VernamСipher:
    def __init__(self, t, key=None):
        self.P = t
        self.len = len(t)
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

    def find_plaintext(self, fragment):
        keyLen = len(fragment)
        possible_keys = []
        for i in range(len(self.C) - keyLen + 1):
            key = [chr(ord(c) ^ ord(k)) for c, k in zip(self.C[i:i + keyLen], fragment)]
            intact_plaintext = "".join(chr(ord(c) ^ ord(k)) for c, k in zip(self.C, key))
            if fragment in intact_plaintext:
                possible_keys.append(''.join(key))
        return possible_keys

if __name__ == "__main__":
    text = VernamСipher(input("Введите открытый текст: "))
    print("Текст:", text.P,
          "\nКлюч:", text.K,
          "\nШифротекст:", text.C)
    print("Декодированный текст:", text.coder(text.K, text.C))
    print("\nВозможные ключи: ", text.find_plaintext(input("Введите фрагмент открытого текста: ")))
