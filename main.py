from generator import generate
from encoder import encrypt_file
from decoder import decode_file
import math

if __name__ == "__main__":
    key = generate(0.5, 0.5, 3, 0.5, math.pi / 2, 128)
    filename = "input.txt"
    encrypt_file(filename, key, 128)
    output_filename = "output.txt"
    decode_file(output_filename, key, 128)
