alphabet = "abcdefghijklmnopqrstuvwxyz"

def ceaserCypher():
    ciphertext = []
    plaintext = input("input plaintext : ")
    plaintext = list(plaintext.lower())
    key = int(input("shift amount : "))
    for letter in plaintext:
        try:
            pos = alphabet.index(letter)
            newpos = (pos + key) % 26
            ciphertext.append(alphabet[newpos])
        except ValueError: 
            ciphertext.append(letter)
            

    print("".join(ciphertext))

def VigenèreCypher():
    ciphertext = []
    plaintext = input("input plaintext : ")
    plaintext = list(plaintext.lower())
    key = input("input cypher key : ")
    key_index = 0
    for letter in plaintext:
        if letter in alphabet:
            pos = alphabet.index(letter)
            keypos = alphabet.index(key[key_index % len(key)])
            newpos = (pos + keypos) % 26
            ciphertext.append(alphabet[newpos])
            key_index += 1
        else:
            ciphertext.append(letter)

    print("".join(ciphertext))









def main():
    choice = int(input("Which Cypher methord would you like to use \n[1] Ceaser Cypher \n[2] Vigenère Cypher \n"))
    match choice:
        case 1:
            ceaserCypher()
        case 2:
            VigenèreCypher()

if __name__ == '__main__':
    main()
    
