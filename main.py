# main.py
from decrypt import Decryptor
from encrypt import Encryptor


def main():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encryptor = Encryptor(alphabet)
    decryptor = Decryptor(alphabet)

    action = int(input("What do u want to do ? \n [1] Encrypt\n [2] Decrypt \n"))
    match action:
        case 1:
            cypher = int(input("Which algorithm do you want to use ? \n[1] Ceaser  \n[2] Vigenère  \n"))
            match cypher:
                case 1:
                    plaintext = input("input plaintext : ").lower()
                    key = int(input("input key : "))
                    encryptor.caesar(plaintext, key)
                case 2:
                    plaintext = input("input plaintext : ").lower()
                    key = input("input key : ").lower()
                    encryptor.vigenere(plaintext, key)
        case 2:
            cypher = int(input("Which algorithm do you want to use ? \n[1] Ceaser  \n[2] Vigenère  \n"))
            match cypher:
                case 1:
                    cyphertext = input("input cyphertext : ").lower()
                    key = int(input("input key : "))
                    decryptor.caesar(cyphertext, key)
                case 2:
                    cyphertext = input("input cyphertext : ").lower()
                    key = input("input key : ").lower()
                    decryptor.vigenere(cyphertext, key)

if __name__ == '__main__':
    main()