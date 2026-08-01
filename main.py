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
            cypher = int(input("Which algorithm do you want to use ? \n[1] Ceaser  \n[2] Vigenère  \n[3] XOR \n"))
            match cypher:
                case 1:
                    plaintext = input("input plaintext : ").lower()
                    key = int(input("input key : "))
                    print(encryptor.caesar(plaintext, key))
                case 2:
                    plaintext = input("input plaintext : ").lower()
                    key = input("input key : ").lower()
                    print(encryptor.vigenere(plaintext, key))
                case 3:
                    plaintext = input("input plaintext : ")
                    key = input("input key : ")
                    print(encryptor.xor(plaintext, key))
        case 2:
            cypher = int(input("Which algorithm do you want to use ? \n[1] Ceaser  \n[2] Vigenère  \n[3] XOR \n"))
            match cypher:
                case 1:
                    cyphertext = input("input cyphertext : ").lower()
                    key = int(input("input key : "))
                    print(decryptor.caesar(cyphertext, key))
                case 2:
                    cyphertext = input("input cyphertext : ").lower()
                    key = input("input key : ").lower()
                    print(decryptor.vigenere(cyphertext, key))
                case 3:
                    cyphertext = input("input cyphertext : ")
                    key = input("input key : ")
                    print(decryptor.xor(cyphertext, key))



if __name__ == '__main__':
    main()