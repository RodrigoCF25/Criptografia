from TextLib import NormalizeText, ALPHABET, ALPHABET_LENGTH
from MatrixLib import Multiply as MatrixMultiply
from MatrixLib import GetMatrixShape, Adjoint, Determinant
from MatrixLib import IsSquare as IsSquareMatrix
from time import time


class HillCipher:
    def __init__(self):
        pass

    def __TextToNumberArrays(self,normalized_plain_text,key):
        """
        normalized_plain_text: string (must be normalized)
        """
        
        message_as_numbers = list(map(lambda letter: ALPHABET.index(letter),normalized_plain_text))
        message_length = len(message_as_numbers)
        

        key_shape = GetMatrixShape(key)

        if message_length % key_shape[0]:
            x_index = ALPHABET.index("x")
            times_to_add = key_shape[0] - message_length % key_shape[0]
            message_as_numbers += [x_index for _ in range(times_to_add)]
            message_length += times_to_add


        p_rows = message_length // key_shape[0]
        p = [[] for _ in range(p_rows)]

        
        for row,start in enumerate(range(0,message_length,key_shape[0])):
            p[row] = message_as_numbers[start:start+key_shape[0]]
        

        return p
    

    
    def __CipherP(self,p,key):
        """
        p: list of lists of integers
        key: list of lists integers [[1,2],[3,4]]
        """
        
        #We have a list of matrix [[[1,2]], [[3,4]]]
        c = list(map(lambda row: MatrixMultiply([row],key)[0],p))

        #We need to convert the result numbers to the alphabet numbers set (0-26) and flatten the list
        for n,row in enumerate(c):
            c[n] = list(map(lambda number: number % ALPHABET_LENGTH,row))
        
        return c



    def Encrypt(self,normalized_plain_text,key):
        """
        normalized_plain_text: string (must be normalized)
        key: list of lists integers [[1,2],[3,4]]
        """

        if not IsSquareMatrix(key):
            raise ValueError("The key must be a square matrix")
        
        normalized_plain_text = NormalizeText(normalized_plain_text)

        try:
            inverse_key = self.__GetInverseKey(key)
        except ValueError as e:
            return str(e) + ", so even encrypting is possible, decrypting is not"

        p =  self.__TextToNumberArrays(normalized_plain_text,key) #We have the message as a list of lists of integers
        
        c = self.__CipherP(p,key) #We have the encrypted message as a list of matrix

        encrypted_text = ["" for _ in range(len(c))]
        
        for n,row in enumerate(c):
            encrypted_text[n] = "".join(map(lambda number: ALPHABET[number],row))
        
        return "".join(encrypted_text)
    


    def __GetModularInverse(self,number):
        """
        number: integer
        """

        for i in range(ALPHABET_LENGTH):
            if (number * i) % ALPHABET_LENGTH == 1:
                #print(f"Modular inverse of {number} is {i}")
                return i
        
        return None



    def __GetInverseKey(self,key):
        """
        key: list of lists integers
        """

        adjoint = Adjoint(key)

        #print(f"Adjoint: {adjoint}")

        rows,columns = GetMatrixShape(key)

        for row in range(rows):
            for column in range(columns):
                    adjoint[row][column] = adjoint[row][column] % ALPHABET_LENGTH
        
        
        #print(f"Adjoint mod 26: {adjoint}")

        determinant = Determinant(key)

        determinant = determinant % ALPHABET_LENGTH

        determinant_modular26_inverse = self.__GetModularInverse(determinant)

        if determinant_modular26_inverse is None:
            raise ValueError("The determinant is not invertible")


        inverse_key = list(map(lambda row: list(map(lambda number: number * determinant_modular26_inverse % ALPHABET_LENGTH,row)),adjoint))

        return inverse_key


    def __DecipherC(self,c,key_inverse):
        """
        c: list of integers
        key_inverse: list of lists integers
        """

        p = list(map(lambda row: MatrixMultiply([row],key_inverse)[0],c))

        for n,row in enumerate(p):
            p[n] = map(lambda number: number % ALPHABET_LENGTH,row)
        
        return p


    def Decrypt(self,cipher_text,key,return_inverse_key=False):
        """
        cipher_text: string
        key: list of lists integers [[1,2],[3,4]]
        """

        try:
            inverse_key = self.__GetInverseKey(key)

        except ValueError as e:
            return str(e) + ", so decrypting is not possible"
        
        c = NormalizeText(cipher_text)

        c = self.__TextToNumberArrays(c,key) #We have the cipher_text as a list of lists of integers


        p = self.__DecipherC(c,inverse_key) #We have the decrypted message as a list of matrix
        
        text_plain = []

        for row in p:
            text_plain.append("".join(map(lambda number: ALPHABET[number],row)))

        text_plain = "".join(text_plain)

        if return_inverse_key:
            return text_plain,inverse_key
        
        return text_plain



    def DecryptKnowingTheInverseKey(self,cipher_text,key_inverse):
        """
        cipher_text: string
        key_inverse: list of lists integers
        """

        c = NormalizeText(cipher_text)

        c = self.__TextToNumberArrays(c,key_inverse)

        p = self.__DecipherC(c,key_inverse)

        text_plain = []

        for row in p:
            text_plain.append("".join(map(lambda number: ALPHABET[number],row)))

        return "".join(text_plain)





if __name__ == "__main__":
    hill_cipher = HillCipher()
    key = [[17,17,5],[21,18,21],[2,2,19]]
    text_plain = "Pay more money"
    normalized_plain_text = NormalizeText(text_plain)
    t1 = time()
    ecnrypted_text = hill_cipher.Encrypt(normalized_plain_text,key)
    t2 = time()
    print(f"Plain text: {text_plain}")
    print(f"Encrypted text: {ecnrypted_text}")
    print(f"Time: {t2-t1} seconds")

    print("\n\n")


    t1 = time()
    text_plain = hill_cipher.Decrypt(ecnrypted_text,key)
    t2 = time()
    print(f"Decrypted text: {text_plain}")
    print(f"Time: {t2-t1} seconds")

    