def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def logical_xor(a, b):
    if bool(a) == bool(b):
        return False
    else:
        return a or b


def encrypt_file(file_name, key, n):
    with open(file_name, "r") as input_file:
        filecontent = input_file.read()

    filecontent_in_bits = ''
    for i in range(len(filecontent)):
        symbol = text_to_bits(filecontent[i])
        filecontent_in_bits += str(symbol)

    temp_key = [0 for i in range(n)]
    for i in range(n):
        temp_key[i] = key[i]

    temp_filecontent_in_bits = [0 for i in range(len(filecontent_in_bits))]
    for i in range(len(filecontent_in_bits)):
        temp_filecontent_in_bits[i] = int(filecontent_in_bits[i])

    i = 0
    j = 0
    while ((n * i + j) < (len(filecontent_in_bits))):
        a = bool(temp_filecontent_in_bits[n * i + j])
        b = bool(temp_key[j])
        temp_filecontent_in_bits[n * i + j] = int(logical_xor(a, b))
        j += 1
        if (j >= n):
            j = 0
            for cnt in range(n):
                temp_key[cnt] = temp_filecontent_in_bits[n * i + cnt]
            i += 1

    filecontent_output = ''.join(map(str, temp_filecontent_in_bits))

    with open("output.txt", "w") as output_file:
        output_file.write(filecontent_output)
