from TextLib import ALPHABET,ALPHABET_LENGTH


#Get the binary representation of a number
def IntToBinary(number):
    return bin(number)[2:]


#Padding a binary number
def PaddingByte(binary_number):
    return "0" * (8 - len(binary_number)) + binary_number


#Get the binary representation of a character
def LetterToBinary(letter):
    letter_index = ALPHABET.index(letter)
    binary_number = IntToBinary(letter_index)
    padded_byte = PaddingByte(binary_number)
    return padded_byte


ALPHABET_BINARY = {letter:LetterToBinary(letter) for letter in ALPHABET}

#Get the binary representation of a text
def TextToBinary(text):
    binary_text = []
    for letter in text:
        binary_text.append(ALPHABET_BINARY[letter])
    
    binary_text = "".join(binary_text)

    return binary_text








#Binary Operations


if __name__ == "__main__":

    number = 10

    binary_number = IntToBinary(number)

    print(binary_number)

    print(ALPHABET_BINARY)

    text = "hello"

    binary_text = TextToBinary(text)

    print(binary_text)
    print(len(binary_text))

    a = 5
    b = 3

    res = a ^ b

    print(res)