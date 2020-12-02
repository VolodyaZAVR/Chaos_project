from generator import generate
from encoder import encrypt_file
from decoder import decode_file
from input import toBinary
from input import toData
import imghdr
import math


if __name__ == "__main__":
    key = generate(0.5, 0.5, 3, 0.5, math.pi / 2, 128)
    filename = "input.txt"
    encrypt_file(filename, key, 128)
    output_filename = "output.txt"
    decode_file(output_filename, key, 128)
    filename = "input.png"
    filetype = imghdr.what(filename)
    binary = toBinary(filename)
    key = generate(0.5, 0.5, 3, 0.5, math.pi / 2, len(binary))
    binaryEncrypt = encrypt_file(binary, key)
    outfile = open("encrypt.txt",'w')
    for i in range(len(binaryEncrypt)):
        outfile.write(str(binaryEncrypt[i]) + ' ')
    outfile.close()
    binaryDecode = decode_file(binaryEncrypt, key)
    toData(binaryDecode,  filetype)
