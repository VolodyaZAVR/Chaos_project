from generator import generate
from encoder import encrypt_file
from decoder import decode_file
from input import toBinary
from input import toData
import math


def isTrue(a, b):
    for i in range(len(a)):
        if (a[i] != b[i]):
            print(i)
            return False
    return True


if __name__ == "__main__":
    filename = "input.jpg"
    binary = toBinary(filename)
    binaryEncrypt = encrypt_file(binary)
    binaryDecode = decode_file(binaryEncrypt)
    toData(binaryDecode)
