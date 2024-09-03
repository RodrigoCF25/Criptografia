from TextLib import ALPHABET,ALPHABET_LENGTH
from time import time

#Get the binary representation of a number
def IntToBinary(number):
    return bin(number)[2:]


def __AND(a,b):
    if a == "1" and b == "1":
        return "1"
    return "0"

def AND(a,b):
    result = list(map(__AND,a,b))
    return "".join(result)

def __OR(a,b):
    if a == "1" or b == "1":
        return "1"
    return "0"

def OR(a,b):
    result = list(map(__OR,a,b))
    return "".join(result)



def __NAND(a,b):
    if __AND(a,b) == "1":
        return "0"
    return "1"

def NAND(a,b):
    result = list(map(__NAND,a,b))
    return "".join(result)


def __NOR(a,b):
    if __OR(a,b) == "1":
        return "0"
    return "1"

def NOR(a,b):
    result = list(map(__NOR,a,b))
    return "".join(result)


def __XOR(a,b):
    if a != b:
        return "1"
    return "0"


def XOR(a,b):
    result = list(map(__XOR,a,b))
    return "".join(result)




    



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
    XOR(a,b)
    t2 = time()
    print(t2-t1,"seconds")