from re import sub as re_sub
from functools import reduce

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_LENGTH = len(ALPHABET)


def NormalizeText(text):
        
        # Lowercase the text
        text = text.lower()

        # Remove special characters
        special_characters = r"[.,:;¡\!¿\?\*\+\-\/\(\)\[\]\{\}\s]+"
        text = re_sub(special_characters, "", text)

        #Change áéíóú to aeiou also ñ to n and ü to u
        letters_to_change = {"á":"a","é":"e","í":"i","ó":"o","ú":"u","ñ":"n","ü":"u"}

        for invalid_letter,valid_letter in letters_to_change.items():
            text = re_sub(invalid_letter,valid_letter,text)

        return text


def GetUniqueValues(text):
    unique_letters = list(reduce(lambda accumulator,letter: accumulator + [letter] if letter not in accumulator else accumulator,text,[]))
    return unique_letters


def NormalizeKey(key):

        if isinstance(key[0],str):

            if isinstance(key,list):
                key = "".join(key)

            key = NormalizeText(key)
            
            notLetters = list(filter(lambda letter: letter not in ALPHABET,key))
            if notLetters:
                raise ValueError("The key must be a string or a list of only letters")
                
            key = [ALPHABET.index(letter) for letter in key]

        elif not isinstance(key[0],int):
            raise ValueError("The key must be a string, a list of integers or a list of letters")
        
        return key

"""
def GetKeyWithTheRightLength(key,text_length):
        key_length = len(key)
        if key_length < text_length:
            quotient = text_length // key_length
            remainder = text_length % key_length
            key = (key * quotient) + key[:remainder]
        
        elif key_length > text_length:
            key = key[:text_length]
        
        return key
"""