from base64 import b64encode
from base64 import b64decode
from io import BytesIO
from PIL import Image
import binascii

def toBinary(filename): #filename = 'F:/py/example.png'
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
            binary[i * 7 + k + delta] = int(temp[2 + k]) #placing binary into array
    return binary

def toData(binary, filetype):
    byteCode = b''
    for i in range(len(binary) // 7):
        charBytes = ''
        for j in range(7):
            charBytes += str(binary[i*7+j])
        charToInt = int(charBytes, 2)
        byteCode += binascii.unhexlify('%x' % charToInt)
    picDecoded = BytesIO(b64decode(byteCode))
    imgRestored = Image.open(picDecoded)
    imgRestored.save("output." + filetype, filetype)




