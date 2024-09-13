from TextLib import PaddingText
from functools import reduce
from BinaryOperations import HexToBinary,BinaryToHex

class SymetricCipher:
    def __init__(self):
        self.hex_digits = "0123456789abcdef"
        self.cache = {}

    def Encrypt(self,plain_text,key):
        pass

    def Decrypt(self, cipher_text,key):
        pass



    def FitTextToKey(self,text,key):
        key_length = len(key)
        text_length = len(text) * 8
        residual = text_length % key_length

        if residual != 0:
            ideal_length = (text_length + key_length - residual) // 8
            text = PaddingText(text,ideal_length)

        return text
    

    def GetBlocks(self,text,size_of_block):
        text_length = len(text)
        blocks = [text[i:i+size_of_block] for i in range(0,text_length,size_of_block)]
        return blocks
    
    
    def BinaryToHex(self,binary_number):
        hex_number = self.cache.get(binary_number)

        if hex_number is None:
            hex_number = BinaryToHex(binary_number)
            
            self.cache[binary_number] = hex_number
            self.cache[hex_number] = binary_number


        return hex_number
    

    def BinaryToHexRepresentation(self,binary_stream):
        hex_stream = (self.BinaryToHex(binary_stream[i:i+4]) for i in range(0,len(binary_stream),4))
        return "".join(hex_stream)


    def HexToBinary(self,hex_number):
        binary_number = self.cache.get(hex_number)

        if binary_number is None:
            binary_number = HexToBinary(hex_number)
            self.cache[hex_number] = binary_number
            self.cache[binary_number] = hex_number


        return binary_number
    
    def HexToBinaryRepresentation(self,hex_stream):
        binary_stream = [self.HexToBinary(hex_stream[i]) for i in range(0,len(hex_stream))]
        return "".join(binary_stream)