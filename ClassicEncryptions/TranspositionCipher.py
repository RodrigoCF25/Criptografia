
from random import shuffle as random_shuffle
from functools import reduce
from time import time
from TextLib import NormalizeText, GetUniqueValues


def CreateKey(length): #Get a key
    key = [i for i in range(length)]
    random_shuffle(key)
    return key

class TranspositionCipher:
    #Consist in rearranging the letters in the text following a certain order, numbers(positions) can't repeat
    def __init__(self):
        pass

    def Encrypt(self,normalizad_plain_text,key):
        """
        text: string (must be normalized)
        key: list of integers
        """        
        
        normalizad_plain_text = NormalizeText(normalizad_plain_text)

        key_length = len(key)
        normalizad_plain_text_length = len(normalizad_plain_text)

        if key_length > normalizad_plain_text_length:
            raise ValueError("Key must have less or equal length than the text")
                
        key_verified_being_unique = GetUniqueValues(key)
        if key_length != len(key_verified_being_unique):
            raise ValueError("The key must have unique numbers")
        
        key = list(filter(lambda index: index < key_length,key))


        if key_length != len(key):
            raise ValueError("The key must have numbers which values are less than the length of the key")
        
        normalizad_plain_text = list(normalizad_plain_text)

        remainder = normalizad_plain_text_length % key_length

        if remainder != 0: #If the text length is not divisible by the key length, we add extra characters to the text
            extra_characters = key_length - (normalizad_plain_text_length % key_length)
            normalizad_plain_text += ["x"]*extra_characters
            normalizad_plain_text_length += extra_characters

        cipher_text = [None] * normalizad_plain_text_length


        for start_index in range(0,normalizad_plain_text_length,key_length):
            end_index = start_index + key_length
            block_text = normalizad_plain_text[start_index:end_index]
            cipher_text[start_index:end_index] = list(map(lambda index: block_text[index],key))

        
        

        return "".join(cipher_text) #Even is shown an error, is impossible to have a None value in plain_text because we checked before that the key and the text have the same length
    


    def Decrypt(self,cipher_text,key):
        """
        text : str
        key : list of integers
        """

        cipher_text = NormalizeText(cipher_text)

        key_length = len(key)
        cipher_text_length = len(cipher_text)

        if cipher_text_length % key_length != 0:
            raise ValueError("The length of the text must be divisible by the length of the key. So it's not the correct text or key")

        if key_length > cipher_text_length:
            raise ValueError("Key must have less or equal length than the text")
                
        key_verified_being_unique = GetUniqueValues(key)
        if key_length != len(key_verified_being_unique):
            raise ValueError("The key must have unique numbers")
        
        key = list(filter(lambda index: index < key_length,key))

        if key_length != len(key):
            raise ValueError("The key must have numbers which values are less than the length of the key")
        
        

        plain_text = [None] * key_length

        for start_index in range(0,cipher_text_length,key_length):
            end_index = start_index + key_length
            block_text = cipher_text[start_index:end_index]
            plain_text[start_index:end_index] = list(map(lambda index: block_text[key.index(index)],range(0,key_length)))

        plain_text = "".join(plain_text) #Even is shown an error, is impossible to have a None value in plain_text because we checked before that the key and the text have the same length


        return plain_text


if __name__ == "__main__":
    encoder = TranspositionCipher()
    print("TranspositionCipher")

    print("Encrypt")
    text = "Springtrap is the best animatronic"
    normalized_text = NormalizeText(text)
    text_length = len(normalized_text)
    #key = [i for i in range(text_length)]
    key = [3,0,2,1]
    random_shuffle(key)
    cipher_text = encoder.Encrypt(normalized_text,key)
    print(f"Original text: {text}")
    print(f"Cipher text: {cipher_text}")
    print(f"My Key: {key}")

    print("")
    print("Decrypt")
    plain_text = encoder.Decrypt(cipher_text,key)
    print(f"Decrypted text: {plain_text}")
    print("-------"*10)

    



    

    


        



        