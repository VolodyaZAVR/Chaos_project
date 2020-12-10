from generator import generate
from encoder import encrypt_file
from decoder import decode_file
from input import toBinary
from input import toData
import imghdr
import math
import os.path

if __name__ == "__main__":
    while True:
        print('Input file name:')
        filename = input()
        if os.path.isfile(filename):
            break
    type_of_file = imghdr.what(filename)

    binary = toBinary(filename)
    with open("input.txt", 'w') as outfile:
        for i in range(len(binary)):
            outfile.write(str(binary[i]))

    key = generate(0.5, 0.5, 3, 0.5, math.pi / 2, len(binary))
    vector_init = generate(0.5, 0.5, 3, 0.5, math.pi / 2, 256)
    for i in range(128):
        vector_init[i] = int(vector_init[128 + i])

    binaryEncrypt = encrypt_file(binary, key, vector_init)
    with open("encrypt.txt", 'w') as outfile:
        for i in range(len(binaryEncrypt)):
            outfile.write(str(binaryEncrypt[i]))

    binaryDecode = decode_file(binaryEncrypt, key, vector_init)
    with open("decode.txt", 'w') as outfile:
        for i in range(len(binaryDecode)):
            outfile.write(str(binaryDecode[i]))
    toData(binaryDecode, type_of_file)
