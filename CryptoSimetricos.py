from time import time
from TextLib import NormalizeText
from SymetricEncryptions.ElectricCodeBook import ElectricCodeBook
from SymetricEncryptions.CipherBlockChaining import CipherBlockChaining
from SymetricEncryptions.DES import DES


if __name__ == "__main__":

    text = "Springtrap is the best animatronic"

    text = NormalizeText(text)

    key = "AF" * 8

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



    print("Encrypting and decrypting using the Cipher Block Chaining")

    initialization_vector = "00" * 8
    key = "AF" * 8

    encoder = CipherBlockChaining()

    t1 = time()
    cipher_text = encoder.Encrypt(text,key,initialization_vector)
    t2 = time()
    print(f"Original text: {text}")
    print(f"Cipher text: {cipher_text}")
    print(f"Time to encrypt: {t2-t1} seconds")


    t1 = time()
    deciphered_text = encoder.Decrypt(cipher_text,key,initialization_vector)
    t2 = time()

    print(f"Deciphered text: {deciphered_text}")
    print(f"Time to decrypt: {t2-t1} seconds")
    print("---------"*10)


    print("Encrypting and decrypting using the DES Encryption")

    encoder = DES()
    key = "AF" * 8

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



