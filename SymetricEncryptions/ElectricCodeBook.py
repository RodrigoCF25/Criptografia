from TextLib import NormalizeText,PaddingText,TextToBinary,BinaryToText
from BinaryOperations import XOR
from MatrixLib import Ceil

class ElectricCodeBook: #ECB
    def __init__(self):
        pass

    def __EncryptBlock(self,block,key):
        block = TextToBinary(block)
        cipher_block = XOR(block,key)
        cipher_block = BinaryToText(cipher_block)
        return cipher_block

    def Encrypt(self,plain_text,key):

        block_size = len(key)
        
        number_of_bits = len(plain_text) * 8
        number_of_blocks = number_of_bits // block_size

        if number_of_blocks == 0 or number_of_bits % block_size != 0:
            number_of_blocks += 1
        
        #The total number of bits must be a multiple of the block size
        number_of_bits = number_of_blocks * block_size
        normalized_plain_text = PaddingText(plain_text,number_of_bits // 8)

        character_per_block = block_size // 8

        plain_text_blocks = [plain_text[i:i+character_per_block] for i in range(0,len(plain_text),character_per_block)]

        
        cipher_text_blocks = []

        for block in plain_text_blocks:
            cipher_block = self.__EncryptBlock(block,key)
            cipher_text_blocks.append(cipher_block)
        
        cipher_text = "".join(cipher_text_blocks)

        return cipher_text
    

    def __DecryptBlock(self,cipher_block,key):
        block = TextToBinary(cipher_block)
        plain_block = XOR(block,key)
        plain_block = BinaryToText(plain_block)
        return plain_block

    def Decrypt(self,cipher_text,key):
        
        block_size = len(key)
        number_of_bits = len(cipher_text) * 8
        number_of_blocks = number_of_bits // block_size

        if number_of_blocks == 0 or number_of_bits % block_size != 0:
            number_of_blocks += 1

        #The total number of bits must be a multiple of the block size
        number_of_bits = number_of_blocks * block_size

        character_per_block = block_size // 8

        cipher_text_blocks = [cipher_text[i:i+character_per_block] for i in range(0,len(cipher_text),character_per_block)]

        plain_text_blocks = []
        
        for block in cipher_text_blocks:
            plain_block = self.__DecryptBlock(block,key)
            plain_text_blocks.append(plain_block)

        plain_text = "".join(plain_text_blocks)
        
        return plain_text



