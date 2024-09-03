from random import shuffle as random_shuffle
from time import time
from TextLib import NormalizeText
from ClassicEncryptions.CaesarCipher import CaesarCipher
from ClassicEncryptions.TranspositionCipher import TranspositionCipher
from ClassicEncryptions.PolyAlphabeticCipher import PolyAlphabeticCipher
from ClassicEncryptions.SubstitutionCipher import SubstitutionCipher
from ClassicEncryptions.PlayfairCipher import PlayfairCipher
from ClassicEncryptions.HillCipher import HillCipher


class Encryptor:
    def __init__(self):
        pass

    
    def CaesarCipher(self,text,shift):
        encoder = CaesarCipher()
        cipher_text = encoder.Encrypt(text,shift)
        return cipher_text
    
    def TranspositionCipher(self,text,key):
        encoder = TranspositionCipher()
        cipher_text = encoder.Encrypt(text,key)
        return cipher_text

    
    def PolyAlphabeticCipher(self,text,key):
        encoder = PolyAlphabeticCipher()
        cipher_text = encoder.Encrypt(text,key)
        return cipher_text
    
    def SubstitutionCipher(self,text,key):
        encoder = SubstitutionCipher()
        cipher_text = encoder.Encrypt(text,key)
        return cipher_text
    
    def PlayfairCipher(self,text,key):
        encoder = PlayfairCipher()
        cipher_text = encoder.Encrypt(text,key)
        return cipher_text

    def HillCipher(self,text,key):
        encoder = HillCipher()
        cipher_text = encoder.Encrypt(text,key)
        return cipher_text


class Decryptor:
    def __init__(self):
        pass

    
    def CaesarCipher(self,text,shift):
        encoder = CaesarCipher()
        plain_text = encoder.Decrypt(text,shift)
        return plain_text
    

    def TranspositionCipher(self,cipher_text,key):
        decoder = TranspositionCipher()
        plain_text = decoder.Decrypt(cipher_text,key)
        return plain_text
    
    def PolyAlphabeticCipher(self,cipher_text,key):
        decoder = PolyAlphabeticCipher()
        plain_text = decoder.Decrypt(cipher_text,key)
        return plain_text
    
    def SubstitutionCipher(self,cipher_text,key):
        decoder = SubstitutionCipher()
        plain_text = decoder.Decrypt(cipher_text,key)
        return plain_text
    
    def PlayfairCipher(self,cipher_text,key):
        decoder = PlayfairCipher()
        plain_text = decoder.Decrypt(cipher_text,key)
        return plain_text
    
    def HillCipher(self,cipher_text,key,return_inverse_key=False):
        decoder = HillCipher()
        plain_text = decoder.Decrypt(cipher_text,key,return_inverse_key)
        return plain_text


if __name__ == "__main__":
    
    encoder = Encryptor()
    decryptor = Decryptor()

    text = "Springtrap is the best animatronic"
    
    normalized_plain_text = NormalizeText(text)
    
    print("Encrypting and decrypting using the Caesar Cipher")
    t1 = time()
    cipher_text = encoder.CaesarCipher(normalized_plain_text,3)
    t2 = time()
    print(f"Original text: {text}")
    print(f"Cipher text: {cipher_text}")
    print(f"Encryption Time: {t2-t1} seconds")
    t1 = time()
    plain_text = decryptor.CaesarCipher(cipher_text,3)
    t2 = time()
    print(f"Decrypted text: {plain_text}")
    print(f"Decryption Time: {t2-t1} seconds")
    print("---------"*10)

    print("Encrypting and decrypting using the PolyAlphabetic Cipher")
    key = "Springtrap"
    t1 = time()
    cipher_text = encoder.PolyAlphabeticCipher(normalized_plain_text,key)
    t2 = time()
    print(f"Original text: {text}")
    print(f"Cipher text: {cipher_text}")
    print(f"Encryption Time: {t2-t1} seconds")
    t1 = time()
    plain_text = decryptor.PolyAlphabeticCipher(cipher_text,key)
    t2 = time()
    print(f"Decrypted text: {plain_text}")
    print(f"Decryption Time: {t2-t1} seconds")
    print("---------"*10)


    print("Encrypting and decrypting using the Transposition Cipher")
    
    key = [3,0,2,1]
    random_shuffle(key)
    t1 = time()
    cipher_text = encoder.TranspositionCipher(normalized_plain_text,key)
    t2 = time()
    print(f"Original text: {text}")
    print(f"Cipher text: {cipher_text}")
    print(f"Encryption Time: {t2-t1} seconds")
    t1 = time()
    plain_text = decryptor.TranspositionCipher(cipher_text,key)
    t2 = time()
    print(f"Decrypted text: {plain_text}")
    print(f"Decryption Time: {t2-t1} seconds")
    print("---------"*10)


    print("Encrypting and decrypting using the Substitution Cipher")
    key = {"b":"c","a":"b","c":"d","d":"e","e":"f","f":"g","g":"h","h":"i","i":"j","j":"k","k":"l","l":"m","m":"n","n":"o","o":"p","p":"q","q":"r","r":"s","s":"t","t":"u","u":"v","v":"w","w":"x","x":"y","y":"z","z":"a"}
    t1 = time()
    cipher_text = encoder.SubstitutionCipher(normalized_plain_text,key)
    t2 = time()
    print(f"Original text: {text}")
    print(f"Cipher text: {cipher_text}")
    print(f"Encryption Time: {t2-t1} seconds")
    t1 = time()
    plain_text = decryptor.SubstitutionCipher(cipher_text,key)
    t2 = time()
    print(f"Decrypted text: {plain_text}")
    print(f"Decryption Time: {t2-t1} seconds")
    print("---------"*10)


    print("Encrypting and decrypting using the Playfair Cipher")
    key = "Springtrap"
    t1 = time()
    cipher_text = encoder.PlayfairCipher(normalized_plain_text,key)
    t2 = time()
    print(f"Original text: {text}")
    print(f"Cipher text: {cipher_text}")
    print(f"Encryption Time: {t2-t1} seconds")

    t1 = time()
    plain_text = decryptor.PlayfairCipher(cipher_text,key)
    t2 = time()
    print(f"Decrypted text: {plain_text}")
    print(f"Decryption Time: {t2-t1} seconds")
    print("---------"*10)


    print("Encrypting and decrypting using the Hill Cipher")
    key = [[17,17,5],[21,18,21],[2,2,19]]
    t1 = time()
    cipher_text = encoder.HillCipher(normalized_plain_text,key)
    t2 = time()
    print(f"Original text: {text}")
    print(f"Cipher text: {cipher_text}")
    print(f"Encryption Time: {t2-t1} seconds")

    t1 = time()
    plain_text = decryptor.HillCipher(cipher_text,key)
    t2 = time()
    print(f"Decrypted text: {plain_text}")
    print(f"Decryption Time: {t2-t1} seconds")
    print("---------"*10)



    print("Tarea Hill Cipher")

    text = "Pay more money"
    key = [[17,17,5],[21,18,21],[2,2,19]]
    cipher_text = encoder.HillCipher(text,key)
    print(f"Original text: {text}")
    print(f"Cipher text: {cipher_text}")
    plain_text,inverse_key = decryptor.HillCipher(cipher_text,key,True)
    print(f"Decrypted text: {plain_text}")
    print(f"Inverse Key: {inverse_key}")
    print("---------"*10)

