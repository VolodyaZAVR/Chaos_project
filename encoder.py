from generator import generate
import math


def logical_xor(a, b):
    if bool(a) == bool(b):
        return 0
    else:
        return 1


def encrypt_file(binary):
    temp_binary = [0] * len(binary)
    for i in range(len(binary)):
        temp_binary[i] = int(binary[i])

    key = generate(0.5, 0.5, 3, 0.5, math.pi / 2, len(temp_binary))

    for i in range(len(temp_binary)):
        temp_binary[i] = logical_xor(temp_binary[i], key[i])

    key = generate(0.5, 0.5, 3, 0.5, math.pi / 2, 256)
    for i in range(128):
        key[i] = key[128 + i]

    i = 0
    j = 0
    while (128 * i + j < len(temp_binary)):
        temp_binary[128 * i + j] = int(logical_xor(temp_binary[128 * i + j], key[j]))
        j += 1
        if (j >= 128):
            i += 1
            for j in range(128):
                key[j] = int(temp_binary[128 * (i - 1) + j])
            j = 0

    for i in range(len(temp_binary)):
        temp_binary[i] = int(temp_binary[i])
    return temp_binary
