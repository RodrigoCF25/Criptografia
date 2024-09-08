from TextLib import PaddingText,TextToBinary,BinaryToText
from BinaryOperations import XOR
from .SymetricCipher import SymetricCipher

class ElectricCodeBook (SymetricCipher):
    def __init__(self):
        super().__init__()

    def __EncryptBlock(self,block,key):
        block = TextToBinary(block)
        cipher_block = XOR(block,key)
        cipher_block = self.BinaryToHexRepresentation(cipher_block)
        return cipher_block

    def Encrypt(self,plain_text,key):
        """
        params:
            plain_text: string (text)
            key: string (hexadecimal)

        returns:
            cipher_text: string (hexadecimal)
        """
        key = key.lower()
        key = self.HexToBinaryRepresentation(key)
        #Not needed because I don´t use padding, I use map method to iterate over the text and the key and map will stop when the shortest iterable is exhausted
        #plain_text = self.FitTextToKey(plain_text,key)

        size_of_block = len(key) // 8

        plain_text_blocks = self.GetBlocks(plain_text,size_of_block)
        
        cipher_text_blocks = []

        for block in plain_text_blocks:
            cipher_block = self.__EncryptBlock(block,key)
            cipher_text_blocks.append(cipher_block)
        
        cipher_text = "".join(cipher_text_blocks)#[:plain_text_length] #The slicing is to remove the padding. But I don´t need to do it because I don´t use padding because I use map method to iterate over the text and the key and map will stop when the shortest iterable is exhausted
        

        return cipher_text
    

    def __DecryptBlock(self,cipher_block,key):
        cipher_block = self.HexToBinaryRepresentation(cipher_block)
        plain_block = XOR(cipher_block,key)
        plain_block = BinaryToText(plain_block)
        return plain_block

    def Decrypt(self,cipher_text,key):
        """
        params:
            cipher_text: string (hexadecimal 4 bits, 8 bits makes a plain text letter)
            key: string (hexadecimal)
        returns:
            plain text: string (text)
        """

        key = key.lower()
        key = self.HexToBinaryRepresentation(key)
        key_length = len(key)

        size_of_block = key_length // 4 #Each letter is represented by 8 bits, so 16 bits (2 hexadecimal digits) makes a letter

        cipher_text_blocks = self.GetBlocks(cipher_text,size_of_block=size_of_block)
        
        plain_text_blocks = []
        
        for block in cipher_text_blocks:
            plain_block = self.__DecryptBlock(block,key)
            plain_text_blocks.append(plain_block)

        plain_text = "".join(plain_text_blocks)
        
        return plain_text



