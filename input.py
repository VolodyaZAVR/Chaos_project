from base64 import b64encode
from base64 import b64decode
from io import BytesIO
from PIL import Image
import binascii

def toBinary(filename):
    with open(filename, 'rb') as file:
        binaryContent = b64encode(file.read())
    binary = [0 for i in range(len(binaryContent) * 7)]
    for i in range(len(binaryContent)):
        temp = bin(binaryContent[i])
        delta = 0
        if len(temp) < 9:
            binary[i * 7] = 0
            delta = 1
        for k in range(len(temp) - 2):
            binary[i * 7 + k + delta] = int(temp[2 + k])#placing binary into array
    return binary

def toBinary1(filename):
    with open(filename, 'rb') as file:
        bin(int.from_bytes(file.read().encode(), 'big'))

def toData(binary):
    picDecoded = BytesIO(b64decode(binary))
    imgRestored = Image.open(picDecoded)
    x = imgRestored.show()

filename = 'F:\САША\Прочее/a.txt'
res = toBinary(filename)
print(res)



