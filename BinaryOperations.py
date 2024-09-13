from TextLib import ALPHABET,ALPHABET_LENGTH
from time import time
from functools import reduce

HEX_DIGITS = "0123456789abcdef"

#Get the binary representation of a number
def IntToBinary(number):
    return bin(number)[2:]


def __AND(a,b):
    if a == "1" and b == "1":
        return "1"
    return "0"

def AND(a,b):
    result = map(__AND,a,b)
    return "".join(result)

def __OR(a,b):
    if a == "1" or b == "1":
        return "1"
    return "0"

def OR(a,b):
    result = map(__OR,a,b)
    return "".join(result)


def __NOT(a):
    if a == "1":
        return "0"
    return "1"


def NOT(a):
    result = map(__NOT,a)
    return "".join(result)

def __NAND(a,b):
    return __NOT(__AND(a,b))

def NAND(a,b):
    result = map(__NAND,a,b)
    return "".join(result)


def __NOR(a,b):
    return __NOT(__OR(a,b))

def NOR(a,b):
    result = map(__NOR,a,b)
    return "".join(result)


def __XOR(a,b):
    if a != b:
        return "1"
    return "0"


def XOR(a,b):
    result = map(__XOR,a,b)
    return "".join(result)


def PaddingBinaryNumber(binary_number,length = 8):
    return "0"*(length-len(binary_number)) + binary_number

    
def BinaryToHex(number):
    bits_reversed = map(lambda bit: bit,number[::-1]) #The bits are reversed
    decimal = reduce(lambda accumulator,bit: accumulator + 2**bit[0] if bit[1] == "1" else accumulator,enumerate(bits_reversed),0) #The number is calculated, bit consits of the index and the value of the bit
    hex_number = HEX_DIGITS[decimal]
    return hex_number


def BinaryToHexRepresentation(binary_stream):
    hex_stream = (BinaryToHex(binary_stream[i:i+4]) for i in range(0,len(binary_stream),4))
    return "".join(hex_stream)


def HexToBinary(hex_number):
    decimal = HEX_DIGITS.index(hex_number)
    binary_number = bin(decimal)[2:]
    binary_number = PaddingBinaryNumber(binary_number,4)

    return binary_number

def HexToBinaryRepresentation(hex_stream):
    binary_stream = (HexToBinary(hex_stream[i]) for i in range(0,len(hex_stream)))
    return "".join(binary_stream)


#Binary Operations


if __name__ == "__main__":

    number = 10

    binary_number = IntToBinary(number)

    print(binary_number)

    a = 5
    b = 3

    res = a ^ b

    print(res)


    a = "01101001 01101100 01110101 01110110 01111001 01100001"
    b = "01111000 01101111 01111000 01101111 01111000 01101111"
    t1 = time()
    print(XOR(a,b))
    t2 = time()
    print(t2-t1,"seconds")