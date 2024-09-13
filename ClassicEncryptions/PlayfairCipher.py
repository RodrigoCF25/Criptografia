from TextLib import NormalizeText, ALPHABET, ALPHABET_LENGTH
from time import time
from functools import reduce

class PlayfairCipher:
    def __init__(self):
        self.key_matrix = []
        self.letters_keyMatrix_positions = dict()

    def __CreateKeyMatrix(self,key):
        
        if False: #Metodo que quita las letras repetidas de la llave y luego rellena con las letras restantes

            key_without_repetitions = reduce(lambda accumulator,letter: accumulator + [letter] if letter not in accumulator else accumulator,key,[])

            key_unique_values = set(key_without_repetitions)

            alphabet = ALPHABET

            alphabet = [letter for letter in alphabet if letter != "j"] #We remove the letter j, because i and j are the same in playfair cipher

            alphabet_set = set(alphabet)

            alphabet_set.difference_update(key_unique_values)

            remaining_letters = sorted(alphabet_set)

            key_matrix = key_without_repetitions + remaining_letters

            key_matrix = [key_matrix[i:i+5] for i in range(0,25,5)]

            return key_matrix
        
        else: #Metodo que reemplaza las letras repetidas en la llave por asteriscos y luego rellena con las letras restantes
            key_cleaned = list()
            key_unique_values = set()

            for letter in key:
                if letter not in key_unique_values:
                    key_cleaned.append(letter)
                    key_unique_values.add(letter)
                else:
                    key_cleaned.append("*")
            
            alphabet = set(ALPHABET)
            alphabet.discard("j")

            alphabet.difference_update(key_unique_values)

            remaining_letters = sorted(alphabet)

            key_cleaned = [letter if letter != "*" else remaining_letters.pop() for letter in key_cleaned]

            key_matrix = key_cleaned + remaining_letters

            key_matrix = [key_matrix[i:i+5] for i in range(0,25,5)]


            return key_matrix


    def __GetLettersPositions(self,key_matrix):
        letters_keyMatrix_positions = dict()
        for row_index,row in enumerate(key_matrix):
            for column_index,letter in enumerate(row):
                letters_keyMatrix_positions[letter] = {"row":row_index,"column":column_index}

        return letters_keyMatrix_positions


    def __SplitTextIntoPairs(self,text):
        text_length = len(text)
        if text_length % 2 != 0:
            text += "x"
            text_length += 1

        pairs = (text[i:i+2] for i in range(0,text_length,2))
        
        return pairs
    

    def __EncryptPair(self,pair):
        letter1 = self.letters_keyMatrix_positions[pair[0]]
        letter2 = self.letters_keyMatrix_positions[pair[1]]

        encripted_letter1 = ""
        encripted_letter2 = ""

        if letter1["row"] == letter2["row"]:
            row = letter1["row"]
            encripted_letter1 = self.key_matrix[row][(letter1["column"] + 1) % 5]
            encripted_letter2 = self.key_matrix[row][(letter2["column"] + 1) % 5]

        elif letter1["column"] == letter2["column"]:
            column = letter1["column"]
            encripted_letter1 = self.key_matrix[(letter1["row"] + 1) % 5][column]
            encripted_letter2 = self.key_matrix[(letter2["row"] + 1) % 5][column]

        else:
            encripted_letter1 = self.key_matrix[letter1["row"]][letter2["column"]]
            encripted_letter2 = self.key_matrix[letter2["row"]][letter1["column"]]
        

        #print(f"Pair: {pair} -> {encripted_letter1}{encripted_letter2}")
            
        return encripted_letter1 + encripted_letter2
    

    def Encrypt(self,normalized_plain_text,key):
        """
        normalized_plain_text: string (must be normalized)
        key: string or list of characters like ["r","a","f","a","e","l"]
        """
        normalized_plain_text = normalized_plain_text.replace("j","i")

        if isinstance(key,list):
            key = "".join(key)
        
        key = NormalizeText(key)

        key = key.replace("j","i")

        if len(key) > 25:
            raise ValueError("The key must have at most 25 characters")

        normalized_plain_text = NormalizeText(normalized_plain_text)

        #We create the key matrix
        self.key_matrix = self.__CreateKeyMatrix(key)


        self.letters_keyMatrix_positions = self.__GetLettersPositions(self.key_matrix)

        #We split the text into pairs of letters
        pairs = self.__SplitTextIntoPairs(normalized_plain_text)

        #We encrypt each pair
        cipher_text = map(lambda pair: self.__EncryptPair(pair),pairs)

        return "".join(cipher_text)
    


    def __DecryptPair(self,pair):
        letter1 = self.letters_keyMatrix_positions[pair[0]]
        letter2 = self.letters_keyMatrix_positions[pair[1]]

        decrypted_letter1 = ""
        decrypted_letter2 = ""

        if letter1["row"] == letter2["row"]:
            row = letter1["row"]
            decrypted_letter1 = self.key_matrix[row][(letter1["column"] - 1) % 5]
            decrypted_letter2 = self.key_matrix[row][(letter2["column"] - 1) % 5]

        elif letter1["column"] == letter2["column"]:
            column = letter1["column"]
            decrypted_letter1 = self.key_matrix[(letter1["row"] - 1) % 5][column]
            decrypted_letter2 = self.key_matrix[(letter2["row"] - 1) % 5][column]

        else:
            decrypted_letter1 = self.key_matrix[letter1["row"]][letter2["column"]]
            decrypted_letter2 = self.key_matrix[letter2["row"]][letter1["column"]]
        

        #print(f"Pair: {pair} -> {decrypted_letter1}{decrypted_letter2}")
            
        return decrypted_letter1 + decrypted_letter2



    def Decrypt(self,cipher_text,key):
        """
        cipher_text: string
        key: string or list of characters like ["r","a","f","a","e","l"] can be of length at most 25
        """

        if isinstance(key,list):
            key = "".join(key)

        
        key = NormalizeText(key)
        key = key.replace("j","i")

        if len(key) > 25:
            raise ValueError("The key must have at most 25 characters")

        cipher_text = NormalizeText(cipher_text)

        #We create the key matrix
        self.key_matrix = self.__CreateKeyMatrix(key)

        self.letters_keyMatrix_positions = self.__GetLettersPositions(self.key_matrix)


        #We split the text into pairs of letters
        pairs = self.__SplitTextIntoPairs(cipher_text)


        #We decrypt each pair
        plain_text = map(lambda pair: self.__DecryptPair(pair),pairs)

        return "".join(plain_text)
    


if __name__ == "__main__":

    #text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec auctor, libero in ultricies gravida, justo leo fermentum dolor, non bibendum nisi purus a nisl. Nullam ac nisl nec purus lacinia tincidunt. Integer et dui nec nunc ultricies ultricies. Nullam sit amet velit nec purus ultricies fermentum. Praesent sed erat nec nisl scelerisque ultricies. Sed non odio nec nisl ultricies fermentum. Curabitur nec nisl nec purus fermentum fermentum. Vestibulum nec nisl nec purus fermentum fermentum fermentum. Nullam nec nisl nec purus fermentum fermentum fermentum fermentum. Nullam nec nisl nec purus fermentum fermentum fermentum fermentum fermentum. Nullam nec nisl nec purus fermentum fermentum fermentum fermentum fermentum fermentum. Nullam nec nisl nec purus fermentum fermentum fermentum fermentum fermentum fermentum fermentum. Nullam nec nisl nec purus fermentum fermentum fermentum fermentum fermentum fermentum fermentum fermentum. Nullam nec nisl nec purus fermentum fermentum fermentum fermentum fermentum fermentum fermentum fermentum fermentum.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec auctor, libero in ultricies gravida, justo leo fermentum dolor, non bibendum nisi purus a nisl. Nullam ac nisl nec purus lacinia tincidunt. Integer et dui nec nunc ultricies ultricies. Nullam sit amet velit nec purus ultricies fermentum. Praesent sed erat nec nisl scelerisque ultricies. Sed non odio nec nisl ultricies fermentum. Curabitur nec nisl nec purus fermentum fermentum. Vestibulum nec nisl nec purus fermentum fermentum fermentum. Nullam nec nisl nec purus fermentum fermentum fermentum fermentum. Nullam nec nisl nec purus fermentum fermentum fermentum fermentum fermentum. Nullam nec nisl nec purus fermentum fermentum fermentum fermentum fermentum fermentum. Nullam nec nisl nec purus fermentum fermentum fermentum fermentum fermentum fermentum fermentum. Nullam nec nisl nec purus fermentum fermentum fermentum fermentum fermentum fermentum fermentum fermentum. Nullam nec nisl nec purus fermentum fermentum fermentum fermentum fermentum fermentum fermentum fermentum fermentum.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec auctor, libero in ultricies gravida, justo leo fermentum dolor, non bibendum nisi purus a nisl. Nullam ac nisl nec purus lacinia tincidunt. Integer et dui nec nunc ultricies ultricies. Nullam sit amet velit nec purus ultricies fermentum. Praesent sed erat nec nisl scelerisque ultricies. Sed non odio nec nisl ultricies fermentum. Curabitur nec nisl nec purus fermentum fermentum. Vestibulum nec nisl nec purus fermentum fermentum fermentum. Nullam nec nisl nec purus fermentum fermentum fermentum fermentum. Nullam nec nisl nec purus fermentum fermentum fermentum fermentum fermentum. Nullam nec nisl nec purus fermentum fermentum fermentum fermentum fermentum fermentum. Nullam nec nisl nec purus fermentum fermentum fermentum fermentum fermentum fermentum fermentum. Nullam nec nisl nec purus fermentum fermentum fermentum fermentum fermentum fermentum fermentum fermentum. Nullam nec nisl nec purus fermentum fermentum fermentum fermentum fermentum fermentum fermentum fermentum fermentum."


   text = "Springtrap is the best animatronic"

   key = "springtrap"
   
   encoder = PlayfairCipher()
   
   cipher_text = encoder.Encrypt(text,key)
   
   print("Cipher text:",cipher_text)
   
   plain_text = encoder.Decrypt(cipher_text,key)

   print("Plain text:",plain_text)

   print("Original text:",text)


   #Tarea

   print("\n\nTarea")

   cipher_text = "difymexrzcectdskvztcpvbitlilixnlqeqdilpvnzzctzenmedtxrntwlwpdzdt"
   
   key = "XHOLI CABDE FGKMN PQRST UVWYZ"

   encoder = PlayfairCipher()
   t1 = time()
   plain_text = encoder.Decrypt(cipher_text,key)
   t2 = time()

   print("Cipher text:",cipher_text)
   print("Plain text:",plain_text)
   print("Decryption Time:",t2-t1,"seconds")
   


