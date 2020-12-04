def logical_xor(a, b):
    if bool(a) == bool(b):
        return 0
    else:
        return 1


def decode_file(binary, key):
    temp_binary = [0] * len(binary)
    for i in range(len(binary)):
        temp_binary[i] = int(binary[i])

    temp_key = [0] * len(key);
    for i in range(len(key)):
        temp_key[i] = int(key[i])

    vectorInit = [0] * 128
    for i in range(128):
        vectorInit[i] = int(key[128 + i])

    i = 0
    j = 0
    while (128 * i + j < len(temp_binary)):
        temp_binary[128 * i + j] = int(logical_xor(temp_binary[128 * i + j], temp_key[128 * i + j]))
        temp_binary[128 * i + j] = int(logical_xor(temp_binary[128 * i + j], vectorInit[j]))
        j += 1
        if (j >= 128):
            i += 1
            for j in range(128):
                vectorInit[j] = int(binary[128 * (i - 1) + j])
            j = 0

    for i in range(len(temp_binary)):
        temp_binary[i] = int(temp_binary[i])
    return temp_binary
