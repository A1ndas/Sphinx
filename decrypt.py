# decrypt.py
class Decryptor:
    def __init__(self, alphabet):
        self.alphabet = alphabet

    def caesar(self, ciphertext, key):
        plaintext = []
        for letter in ciphertext:
            try:
                pos = self.alphabet.index(letter)
                newpos = (pos - key) % 26
                plaintext.append(self.alphabet[newpos])
            except ValueError: 
                plaintext.append(letter)
        print("".join(plaintext))


    def vigenere(self, ciphertext, key):
        pass