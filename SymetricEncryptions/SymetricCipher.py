from TextLib import PaddingText

class SymetricCipher:
    def __init__(self):
        self.cache = {}

    def encrypt(self,plain_text,key):
        pass

    def decrypt(self, cipher_text,key):
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
    