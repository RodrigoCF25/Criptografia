from TextLib import PaddingText,TextToBinary,BinaryToText
from BinaryOperations import XOR
from .SymetricCipher import SymetricCipher

class ElectricCodeBook (SymetricCipher):
    def __init__(self):
        pass

    def __EncryptBlock(self,block,key):
        block = TextToBinary(block)
        cipher_block = XOR(block,key)
        cipher_block = BinaryToText(cipher_block)
        return cipher_block

    def Encrypt(self,plain_text,key):

        key_length = len(key)
   
        #Not needed because I don´t use padding, I use map method to iterate over the text and the key and map will stop when the shortest iterable is exhausted
        #plain_text = self.FitTextToKey(plain_text,key)

        character_per_block = key_length // 8

        plain_text_blocks = [plain_text[i:i+character_per_block] for i in range(0,len(plain_text),character_per_block)]

        
        cipher_text_blocks = []

        for block in plain_text_blocks:
            cipher_block = self.__EncryptBlock(block,key)
            cipher_text_blocks.append(cipher_block)
        
        cipher_text = "".join(cipher_text_blocks)#[:plain_text_length] #The slicing is to remove the padding. But I don´t need to do it because I don´t use padding because I use map method to iterate over the text and the key and map will stop when the shortest iterable is exhausted
        

        return cipher_text
    

    def __DecryptBlock(self,cipher_block,key):
        block = TextToBinary(cipher_block)
        plain_block = XOR(block,key)
        plain_block = BinaryToText(plain_block)
        return plain_block

    def Decrypt(self,cipher_text,key):
        
        key_length = len(key)
        """
        cipher_text_length = len(cipher_text)
        residual = cipher_text_length % key_length

        if residual != 0:
            ideal_length = (cipher_text_length + key_length - residual)//8
            cipher_text = PaddingText(cipher_text,ideal_length)
        """

        character_per_block = key_length // 8

        cipher_text_blocks = [cipher_text[i:i+character_per_block] for i in range(0,len(cipher_text),character_per_block)]

        plain_text_blocks = []
        
        for block in cipher_text_blocks:
            plain_block = self.__DecryptBlock(block,key)
            plain_text_blocks.append(plain_block)

        plain_text = "".join(plain_text_blocks)
        
        return plain_text



