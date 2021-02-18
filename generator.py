import math


def generate_key(x0, y0, k, s, alpha, n):
    x = x0
    y = y0
    key = [0 for i in range(n)]
    for i in range(n):
        xn = math.cos(alpha) * x + math.sin(alpha) * (y + k * s * math.sin(x))
        xn = math.fmod(xn, 1)
        b = int(math.fmod(abs(int(xn * 10 ** 9)), 2))
        yn = -math.sin(alpha) * x + math.cos(alpha) * (y + k * s * math.sin(x)) + (1 - s) * k * math.sin(xn)
        yn = math.fmod(yn, 1)
        x = xn
        y = yn
        key[i] = b
    return key
