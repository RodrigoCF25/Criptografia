from time import time
from TextLib import NormalizeText
from SymetricEncryptions.ElectricCodeBook import ElectricCodeBook



if __name__ == "__main__":

    text = "Springtrap is the best animatronic"

    text = NormalizeText(text)

    key = "10101010" * 8

    encoder = ElectricCodeBook()

    print("Encrypting and decrypting using the Electric Code Book")
    t1 = time()
    cipher_text = encoder.Encrypt(text,key)
    t2 = time()
    print(f"Original text: {text}")
    print(f"Cipher text: {cipher_text}")
    print(f"Time to encrypt: {t2-t1} seconds")

    t1 = time()
    deciphered_text = encoder.Decrypt(cipher_text,key)
    t2 = time()

    print(f"Deciphered text: {deciphered_text}")
    print(f"Time to decrypt: {t2-t1} seconds")
    print("---------"*10)

