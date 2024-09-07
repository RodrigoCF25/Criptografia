from TextLib import PaddingText,TextToBinary,BinaryToText
from BinaryOperations import XOR, IntToBinary, PaddingBinaryNumber
from SymetricEncryptions.SymetricCipher import SymetricCipher


class CipherBlockChaining(SymetricCipher):

    def __init__(self):
        """
        This Cipher cant be executed concurrently, because it needs the previous cipher block to encrypt the next block
        """
        pass

    def __EncryptBlock(self,block,key,previous_cipher_block):
        block = TextToBinary(block)
        xored_block = XOR(block,previous_cipher_block)
        cipher_block = XOR(xored_block,key)
        return cipher_block

    def Encrypt(self,plain_text,key,initialization_vector):
        """
        returns binary text
        """
        key_length = len(key)
        #plain_text = self.FitTextToKey(plain_text,key) Don´t need to use padding because I use map method to iterate over the text and the key and map will stop when the shortest iterable is exhausted
        character_per_block = key_length // 8

        plain_text_blocks = [plain_text[i:i+character_per_block] for i in range(0,len(plain_text),character_per_block)]

        cipher_text_blocks = []

        previous_cipher_block = initialization_vector

        for block in plain_text_blocks:
            cipher_block = self.__EncryptBlock(block,key,previous_cipher_block)
            previous_cipher_block = cipher_block
            cipher_text_blocks.append(cipher_block)

        return "".join(cipher_text_blocks)


    def __DecryptBlock(self,cipher_block,key,previous_cipher_block):
        xored_block = XOR(cipher_block,key)
        plain_block = XOR(xored_block,previous_cipher_block)
        return plain_block

    def Decrypt(self, cipher_text,key,initialization_vector):
        """
        cipher_text: string (binary)
        """


        cipher_text_length = len(cipher_text)
        key_length = len(key)

        
        cipher_text_blocks = [cipher_text[i:i+key_length] for i in range(0,cipher_text_length,key_length)]

        plain_text_blocks = []
        previous_cipher_block = initialization_vector

        for block in cipher_text_blocks:
            plain_block = self.__DecryptBlock(block,key,previous_cipher_block)
            previous_cipher_block = block
            plain_block = BinaryToText(plain_block)
            plain_text_blocks.append(plain_block)
        
        plain_text = "".join(plain_text_blocks)

        return plain_text

