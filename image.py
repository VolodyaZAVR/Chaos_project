from base64 import b64encode
from base64 import b64decode
from io import BytesIO
from PIL import Image
import binascii


def convert_to_binary(filename):
    with open(filename, 'rb') as file:
        binary_content = b64encode(file.read())
    binary = [0 for i in range(len(binary_content) * 7)]
    for i in range(len(binary_content)):
        temp = bin(binary_content[i])
        delta = 0
        if len(temp) < 9:
            binary[i * 7] = 0
            delta = 1
        for k in range(len(temp) - 2):
            binary[i * 7 + k + delta] = int(temp[2 + k])
    return binary


def convert_to_data(binary, filetype):
    byte_code = b''
    for i in range(len(binary) // 7):
        char_bytes = ''
        for j in range(7):
            char_bytes += str(binary[i * 7 + j])
        char_to_int = int(char_bytes, 2)
        byte_code += binascii.unhexlify('%x' % char_to_int)
    pic_decoded = BytesIO(b64decode(byte_code))
    img_restored = Image.open(pic_decoded)
    img_restored.save("output." + filetype, filetype)
