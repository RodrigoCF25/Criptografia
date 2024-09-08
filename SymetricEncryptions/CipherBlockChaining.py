from TextLib import PaddingText,TextToBinary,BinaryToText
from BinaryOperations import XOR, IntToBinary, PaddingBinaryNumber
from SymetricEncryptions.SymetricCipher import SymetricCipher


class CipherBlockChaining(SymetricCipher):

    def __init__(self):
        """
        This Cipher cant be executed concurrently, because it needs the previous cipher block to encrypt the next block
        """
        super().__init__()

    def __EncryptBlock(self,block,key,previous_cipher_block):
        """
        
        """
        block = TextToBinary(block)
        xored_block = XOR(block,previous_cipher_block)
        cipher_block = XOR(xored_block,key)
        return cipher_block

    def Encrypt(self,plain_text,key,initialization_vector):
        """
        returns binary text represented by hexadecimal digits
        """
        
        key = key.lower()
        key = self.HexToBinaryRepresentation(key)

        initialization_vector = initialization_vector.lower()
        initialization_vector = self.HexToBinaryRepresentation(initialization_vector)

        #plain_text = self.FitTextToKey(plain_text,key) Don´t need to use padding because I use map method to iterate over the text and the key and map will stop when the shortest iterable is exhausted
        
        size_of_block = len(key) // 8

        plain_text_blocks = self.GetBlocks(plain_text,size_of_block)

        cipher_text_blocks = []

        previous_cipher_block = initialization_vector

        for block in plain_text_blocks:
            cipher_block = self.__EncryptBlock(block,key,previous_cipher_block)
            previous_cipher_block = cipher_block
            hex_cipher_block = self.BinaryToHexRepresentation(cipher_block)
            cipher_text_blocks.append(hex_cipher_block)


        return "".join(cipher_text_blocks)


    def __DecryptBlock(self,cipher_block,key,previous_cipher_block):
        """
        returns:
        plain text block: string (text)
        cipher_block: string (binary)
        """
        xored_block = XOR(cipher_block,key)
        plain_text_block = BinaryToText(XOR(xored_block,previous_cipher_block))
        return plain_text_block

    def Decrypt(self, cipher_text,key,initialization_vector):
        """
        cipher_text: string (hexadecimal 4 bits, 8 bits makes a plain text letter)
        returns plain text
        """

        key = key.lower()
        key = self.HexToBinaryRepresentation(key)

        initialization_vector = initialization_vector.lower()
        initialization_vector = self.HexToBinaryRepresentation(initialization_vector)

        key_length = len(key)
        size_of_block = key_length // 4 #Each letter is represented by 8 bits, so 16 bits (2 hexadecimal digits) makes a letter
        cipher_text_blocks = self.GetBlocks(cipher_text,size_of_block=size_of_block)


        plain_text_blocks = []
        previous_cipher_block = initialization_vector

        for block in cipher_text_blocks:
            block = self.HexToBinaryRepresentation(block)
            plain_text_block = self.__DecryptBlock(block,key,previous_cipher_block)
            previous_cipher_block = block
            plain_text_blocks.append(plain_text_block)
        
        plain_text = "".join(plain_text_blocks)

        return plain_text

