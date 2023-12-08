from input_utils import load_input
import math

# PART I, II

def square_roots(a, b, c):
    delta = b**2 - 4 * a * c
    return (-b + delta**.5)/(2*a), (-b - delta**.5)/(2*a)

data = load_input().splitlines()
times, distances = data[0].split(":")[1].split(), data[1].split(":")[1].split()

product = 1
for t, d in zip(times, distances):
    a, b = square_roots(-1, int(t), -int(d))
    print(a, b, end=" => ")
    t = int(t)
    a = min(t, math.ceil(a+0.0001))
    b = min(t, math.floor(b-0.0001))
    print(a, b)
    product *= (b - a + 1)
    print((b - a + 1))

print("Result 1:", product)