from generator import generate
import math

if __name__ == "__main__":
    key = generate(0.5, 0.5, 3, 0.5, math.pi / 2, 128)
    print(*key)
