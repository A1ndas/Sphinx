alphabet = "abcdefghijklmnopqrstuvwxyz"

def ceaserCypher():
    plaintext = input("input plaintext : ")
    ciphertext = []
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

def main():
    choice = int(input("Which Cypher methord would you like to use \n[1] Ceaser Cypher \n"))
    match choice:
        case 1:
            ceaserCypher()

if __name__ == '__main__':
    main()
    
