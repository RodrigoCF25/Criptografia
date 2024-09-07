from .SymetricCipher import SymetricCipher
from TextLib import TextToBinary


class DES(SymetricCipher):
    def __init__(self):
        self.__initial_permutation = [58, 50, 42, 34, 26, 18, 10, 2,
                                    60, 52, 44, 36, 28, 20, 12, 4,
                                    62, 54, 46, 38, 30, 22, 14, 6,
                                    64, 56, 48, 40, 32, 24, 16, 8,
                                    57, 49, 41, 33, 25, 17, 9, 1,
                                    59, 51, 43, 35, 27, 19, 11, 3,
                                    61, 53, 45, 37, 29, 21, 13, 5,
                                    63, 55, 47, 39, 31, 23, 15, 7]
        
        self.__inverse_initial_permutation = [40, 8, 48, 16, 56, 24, 64, 32,
                                            39, 7, 47, 15, 55, 23, 63, 31,
                                            38, 6, 46, 14, 54, 22, 62, 30,
                                            37, 5, 45, 13, 53, 21, 61, 29,
                                            36, 4, 44, 12, 52, 20, 60, 28,
                                            35, 3, 43, 11, 51, 19, 59, 27,
                                            34, 2, 42, 10, 50, 18, 58, 26,
                                            33, 1, 41, 9, 49, 17, 57, 25]
        
        self.__expansion = [32, 1, 2, 3, 4, 5,
                        4, 5, 6, 7, 8, 9,
                        8, 9, 10, 11, 12, 13,
                        12, 13, 14, 15, 16, 17,
                        16, 17, 18, 19, 20, 21,
                        20, 21, 22, 23, 24, 25,
                        24, 25, 26, 27, 28, 29,
                        28, 29, 30, 31, 32, 1]
        
        self.__permutation_function = [16, 7, 20, 21, 29, 12, 28, 17,
                                    1, 15, 23, 26, 5, 18, 31, 10,
                                    2, 8, 24, 14, 32, 27, 3, 9,
                                    19, 13, 30, 6, 22, 11, 4, 25]
        

        self.__permutation_choice1 = [57, 49, 41, 33, 25, 17, 9,
                                    1, 58, 50, 42, 34, 26, 18,
                                    10, 2, 59, 51, 43, 35, 27,
                                    19, 11, 3, 60, 52, 44, 36,
                                    63, 55, 47, 39, 31, 23, 15,
                                    7, 62, 54, 46, 38, 30, 22,
                                    14, 6, 61, 53, 45, 37, 29,
                                    21, 13, 5, 28, 20, 12, 4]
        

    def __Permute(self,text,permutation):
        return "".join([text[i-1] for i in permutation])
    
    def __DoPermutationChoice1(self,key):
        return self.__Permute(key,self.__permutation_choice1)


    def __DoInitialPermutation(self,text):
        return self.__Permute(text,self.__initial_permutation)
    

    def __DoExpansionPermutation(self,text):
        return self.__Permute(text,self.__expansion)
    

    def __EncryptBlock(self,block,key):
        block = TextToBinary(block)
        block = self.__DoInitialPermutation(block)

        left_block = block[:32] #Li-1
        right_block = block[32:] #Ri-1

        right_block = self.__DoExpansionPermutation(right_block) #Now right_block has 48 bits

        left_key = key[:28] #Ci-1
        right_key = key[28:] #Di-1





    def Encrypt(self,plain_text,key):
        
        plain_text = self.FitTextToKey(plain_text,key) 
        size_of_block = len(key) // 8
        plain_text_blocks = self.GetBlocks(plain_text,size_of_block)

        key = self.__DoPermutationChoice1(key) #56 bits


        for block in plain_text_blocks:
            self.__EncryptBlock(block,key)
            break
            






    def Decrypt(self,cipher_text,key):
        pass

   
    def __DecryptBlock(self,cipher_block,key):
        pass