from myText import ALPHABET, ALPHABET_LENGTH, NormalizeText, NormalizeKey, GetUniqueValues
from functools import reduce
from time import time
from random import choice


class SubstitutionCipher:

    def __init__(self):
        pass

    def Encrypt(self,normalized_plain_text,substitution_key):
        """

        normalized_plain_text: string (must be normalized)
        substitution_key: dictionary

        """
        
        normalized_plain_text = normalized_plain_text.lower()

        cipher_text = list(map(lambda letter: substitution_key[letter],normalized_plain_text))

        

        return "".join(cipher_text)
    


    def Decrypt(self,cipher_text,substitution_key):
        """
        cipher_text: string
        substitution_key: dictionary
        """

        

        inverted_key = {value:key for key,value in substitution_key.items()}

        plain_text = list(map(lambda letter: inverted_key[letter],cipher_text))


        return "".join(plain_text)
       

        
        
       

        

if __name__ == "__main__":

    text = "Springtrap is the best animatronic"
    key = {"b":"c","a":"b","c":"d","d":"e","e":"f","f":"g","g":"h","h":"i","i":"j","j":"k","k":"l","l":"m","m":"n","n":"o","o":"p","p":"q","q":"r","r":"s","s":"t","t":"u","u":"v","v":"w","w":"x","x":"y","y":"z","z":"a"}
    normalized_plain_text = NormalizeText(text)
    encoder = SubstitutionCipher()
    cipher_text = encoder.Encrypt(normalized_plain_text,key)
        
    print(f"Original text: {text}")
    print(f"Cipher text: {cipher_text}")

    plain_text = encoder.Decrypt(cipher_text,key)
    print(f"Decrypted text: {plain_text}")
