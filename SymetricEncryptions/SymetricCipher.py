from TextLib import PaddingText

class SymetricCipher:
    def __init__(self):
        pass

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
    