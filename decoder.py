def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'


def logical_xor(a, b):
    if bool(a) == bool(b):
        return False
    else:
        return a or b


def decode_file(filename, key, n):
    with open(filename, "r") as input_file:
        filecontent = input_file.read()

    temp_key = [0 for i in range(n)]
    for i in range(n):
        temp_key[i] = key[i]

    temp_filecontent = [0 for i in range(len(filecontent))]
    for i in range(len(filecontent)):
        temp_filecontent[i] = int(filecontent[i])

    result_filecontent = [0 for i in range(len(filecontent))]

    i = 0
    j = 0
    while ((n * i + j) < (len(temp_filecontent))):
        a = bool(temp_filecontent[n * i + j])
        b = bool(temp_key[j])
        result_filecontent[n * i + j] = str(int(logical_xor(a, b)))
        j += 1
        if (j >= n):
            j = 0
            for cnt in range(n):
                temp_key[cnt] = temp_filecontent[n * i + cnt]
            i += 1

    temp_string = ''.join(map(str, result_filecontent))
    filecontent_output = text_from_bits(temp_string)

    with open("result.txt", "w") as output_file:
        output_file.write(filecontent_output)


