def logical_xor(a, b):
    if bool(a) == bool(b):
        return 0
    else:
        return 1


def decode_file(binary, key, vector):
    temp_binary = [0] * len(binary)
    for i in range(len(binary)):
        temp_binary[i] = int(binary[i])

    vector_init = [0] * 128
    for i in range(128):
        vector_init[i] = int(vector[i])

    i = 0
    j = 0
    while (128 * i + j < len(temp_binary)):
        temp_binary[128 * i + j] = int(logical_xor(temp_binary[128 * i + j], key[128 * i + j]))
        temp_binary[128 * i + j] = int(logical_xor(temp_binary[128 * i + j], vector_init[j]))
        j += 1
        if (j >= 128):
            i += 1
            for j in range(128):
                vector_init[j] = int(binary[128 * (i - 1) + j])
            j = 0
    return temp_binary
