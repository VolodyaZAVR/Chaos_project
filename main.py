from generator import generate
from encoder import encrypt_file
from decoder import decode_file
from input import toBinary
from input import toData
import math

if __name__ == "__main__":
    filename = "input.jpg"
    binary = toBinary(filename)
    key = generate(0.5, 0.5, 3, 0.5, math.pi / 2, len(binary))
    binaryEncrypt = encrypt_file(binary, key)
    binaryDecode = decode_file(binaryEncrypt, key)
    toData(binaryDecode)
