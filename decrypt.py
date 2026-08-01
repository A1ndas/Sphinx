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
        return "".join(plaintext)


    def vigenere(self, cyphertext, key):
        plaintext = []
        key_index = 0
        for letter in cyphertext:
            if letter in self.alphabet:
                pos = self.alphabet.index(letter)
                keypos = self.alphabet.index(key[key_index % len(key)])
                newpos = (pos - keypos) % 26
                plaintext.append(self.alphabet[newpos])
                key_index += 1
            else:
                plaintext.append(letter)
        return "".join(plaintext)

    def xor(self, cyphertext, key):
        plaintext = []
        cyphertext = list(bytes.fromhex(cyphertext))
        for i, letter in enumerate(cyphertext):
            result = chr(letter ^ ord(key[i % len(key)]))
            plaintext.append(result)
        return "".join(plaintext)