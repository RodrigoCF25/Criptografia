from TextLib import ALPHABET, ALPHABET_LENGTH, NormalizeText, NormalizeKey
from time import time

class PolyAlphabeticCipher:
    def __init__(self):
        pass


    def Encrypt(self,normalized_plain_text,key):
        """
        key: string or list of integers or list of strings
        """

        normalized_plain_text = NormalizeText(normalized_plain_text)

        key = NormalizeKey(key)

        #So now, the key is for sure a list of integers

        
        #Now we check if the key has the same length as the text
        #If not, we repeat the key until it has the same length as the text
        key_length = len(key)
        text_length = len(normalized_plain_text)
        
        if key_length > text_length:
            key = key[:text_length]
            key_length = text_length

        number_of_blocks = text_length // key_length 
        if number_of_blocks * key_length < text_length:
            number_of_blocks += 1

        cipher_text = [None] * number_of_blocks 
        

        for start_index in range(0,text_length,key_length):
            end_index = start_index + key_length
            block_text = normalized_plain_text[start_index:end_index]
            block_cipher_text = map(lambda letter,key_item: ALPHABET[(ALPHABET.index(letter) + key_item) % ALPHABET_LENGTH],block_text,key)
            cipher_text[start_index:end_index] = "".join(block_cipher_text)

        
        cipher_text = "".join(cipher_text)

        
        
        return cipher_text


    def Decrypt(self,cipher_text,key):
        """
        key: string or list of integers or list of strings
        """

        cipher_text = NormalizeText(cipher_text)

        key = NormalizeKey(key)

        #So now,the key is for sure a list of integers

        
        #Now we check if the key has the same length as the text
        #If not, we repeat the key until it has the same length as the text
        key_length = len(key)
        cipher_text_length = len(cipher_text)

        if key_length > cipher_text_length:
            key = key[:cipher_text_length]
            key_length = cipher_text_length
        
        number_of_blocks = cipher_text_length // key_length
        if number_of_blocks * key_length < cipher_text_length:
            number_of_blocks += 1


        plain_text = [None] * number_of_blocks

        for start_index in range(0,cipher_text_length,key_length):
            end_index = start_index + key_length
            block_text = cipher_text[start_index:end_index]
            block_plain_text = map(lambda letter,key_item: ALPHABET[(ALPHABET.index(letter) - key_item) % ALPHABET_LENGTH],block_text,key)
            plain_text[start_index:end_index] = "".join(block_plain_text)

        plain_text = "".join(plain_text)

        
        
        return plain_text

if __name__ == "__main__":
    text = NormalizeText("Springtrap is the best animatronic")

    key = "Springtrap"


    encoder = PolyAlphabeticCipher()
    cipher_text = encoder.Encrypt(text,key)

    print(cipher_text)

    plain_text = encoder.Decrypt(cipher_text,key)

    print(plain_text)
