# encrypt.py
class Encryptor:
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    def caesar(self, plaintext, key):
        ciphertext = []
        for letter in plaintext:
            try:
                pos = self.alphabet.index(letter)
                newpos = (pos + key) % 26
                ciphertext.append(self.alphabet[newpos])
            except ValueError: 
                ciphertext.append(letter)
        return "".join(ciphertext)
            


    def vigenere(self, plaintext, key):
        ciphertext = []
        key_index = 0
        for letter in plaintext:
            if letter in self.alphabet:
                pos = self.alphabet.index(letter)
                keypos = self.alphabet.index(key[key_index % len(key)])
                newpos = (pos + keypos) % 26
                ciphertext.append(self.alphabet[newpos])
                key_index += 1
            else:
                ciphertext.append(letter)
        return "".join(ciphertext)

    def xor(self, plaintext, key):
        result_bytes = []
        for i, letter in enumerate(plaintext):
            result = ord(letter) ^ ord(key[i % len(key)])
            result_bytes.append(result)
        return bytes(result_bytes).hex()