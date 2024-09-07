from TextLib import PaddingText,TextToBinary,BinaryToText

from BinaryOperations import XOR
from SymetricCiphers import SymetricCipher

class CipherBlockChaining(SymetricCipher):

    def __init__(self):
        """This Cipher cant be executed concurrently, because it needs the previous cipher block to encrypt the next block"""
        pass

    def __EncryptBlock(self,block,key,previous_cipher_block):
        xored_block = XOR(block,previous_cipher_block)
        cipher_block = XOR(xored_block,key)
        return cipher_block

    def Encrypt(self,plain_text,key,initialization_vector):

        pass


    def __DecryptBlock(self,cipher_block,key,previous_cipher_block):
        xored_block = XOR(cipher_block,key)
        plain_block = XOR(xored_block,previous_cipher_block)
        return plain_block

    def Decrypt():
        pass

