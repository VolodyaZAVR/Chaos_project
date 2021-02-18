from generator import generate_key
from encryption import encrypt_binary_data
from encryption import decode_file
from image import convert_to_binary
from image import convert_to_data
import imghdr
import math
import os.path


def write_in_file(filename, message):
    with open(filename, 'w') as outfile:
        for i in range(len(message)):
            outfile.write(str(message[i]))


def encrypt_file(filename):
    binary = convert_to_binary(filename)
    key = generate_key(0.5, 0.5, 3, 0.5, math.pi / 2, len(binary))
    vector_init = generate_key(0.5, 0.5, 3, 0.5, math.pi / 2, 256)
    for i in range(128):
        vector_init[i] = int(vector_init[128 + i])

    binary_encrypt = encrypt_binary_data(binary, key, vector_init)


def main():
    while True:
        print('Input file name:')
        filename = input()
        if os.path.isfile(filename):
            break
        else:
            print('File doesnt exist.')
    filetype = imghdr.what(filename)

    binary = convert_to_binary(filename)

    key = generate_key(0.5, 0.5, 3, 0.5, math.pi / 2, len(binary))
    vector_init = generate_key(0.5, 0.5, 3, 0.5, math.pi / 2, 256)
    for i in range(128):
        vector_init[i] = int(vector_init[128 + i])

    binary_encrypt = encrypt_binary_data(binary, key, vector_init)
    write_in_file('encrypt.txt', binary_encrypt)

    binary_decode = decode_file(binary_encrypt, key, vector_init)
    write_in_file('decode.txt', binary_decode)
    convert_to_data(binary_decode, filetype)


if __name__ == '__main__':
    main()
