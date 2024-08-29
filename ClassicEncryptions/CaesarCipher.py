from TextLib import ALPHABET, ALPHABET_LENGTH, NormalizeText
from time import time

class CaesarCipher:
    def __init__(self):
        pass

    def Encrypt(self,normalized_plain_text,shift):
        """
        normalized_plain_text: string (must be normalized)
        """

        normalized_plain_text = NormalizeText(normalized_plain_text)
        cipher_text = list()

        for letter in normalized_plain_text:
            old_index = ALPHABET.index(letter)
            new_index = (old_index + shift) % ALPHABET_LENGTH
            new_letter = ALPHABET[new_index]
            cipher_text.append(new_letter)
        
        return "".join(cipher_text)
    
    def Decrypt(self,cipher_text,shift):
        plain_text = list()

        cipher_text = NormalizeText(cipher_text)
        
        for letter in cipher_text:
            old_index = ALPHABET.index(letter)
            new_index = (old_index - shift) % ALPHABET_LENGTH
            new_letter = ALPHABET[new_index]
            plain_text.append(new_letter)
        
        return "".join(plain_text)


if __name__ == "__main__":
        
    text = "Hola, ¿cómo estás? ¿Qué tal tu día? ¿Estás bien?"
    normalized_plain_text = NormalizeText(text)
    encoder = CaesarCipher()
    cipher_text = encoder.Encrypt(normalized_plain_text,3)
    print(f"Original text: {text}")
    print(f"Cipher text: {cipher_text}")
    plain_text = encoder.Decrypt(cipher_text,3)
    print(f"Decrypted text: {plain_text}")



    #Tarea

    cipher_text = "wpn bjrwph rdhph tmigpcph tc thit bjcsd, idsdh adh sxph drjggtc wtrwdh fjt cd ejtstc htg tmeaxrpsdh, utcdbtcdh tmigpdgsxcpgxdh fjt ephpc sthpetgrxqxsdh edgfjt ap vtcit rxtggp hjh dydh p ad fjt cd tcixtcst, etgd ap ktgsps th fjt st idsph aph rdhph xctmeaxrpqath st thit bjcsd ap wjbpcxsps th ap bph tmigpcp st idsph."

    decryptor = CaesarCipher()

    for shift in range(1,26):
        plain_text = decryptor.Decrypt(cipher_text,shift)
        print(f"Shift: {shift}")
        print(f"Plain text: {plain_text}")
        print("\n\n")


        