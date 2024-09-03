from re import sub as re_sub
from functools import reduce

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_LENGTH = len(ALPHABET)


def NormalizeText(text):
        
        # Lowercase the text
        text = text.lower()

        pattern = r"[^a-zA-Z0-9\s]+|[\d\s]+"

        # Remove all non-alphabetic characters
        text = re_sub(pattern,"",text)

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


def PaddingText(text,length):
    text = text + "x"*(length - len(text))
    return text



def LetterToBinary(letter):
    letter_number = ord(letter)
    binary_number = bin(letter_number)[2:]
    binary_number = "0"*(8-len(binary_number)) + binary_number
    return binary_number


def TextToBinary(text):
    binary_text = [LetterToBinary(letter) for letter in text]
    return "".join(binary_text)


def BinaryToLetter(binary):
    letter_number = int(binary,2)
    letter = chr(letter_number)
    return letter

def BinaryToText(binary_text):
    text = list(map(BinaryToLetter,[binary_text[i:i+8] for i in range(0,len(binary_text),8)]))
    return "".join(text)


