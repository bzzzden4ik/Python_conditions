from math import *

# 7 вариант
def find_y(a, b, x):
    return exp**(-2 * x) + (a**4 + x)**(1.0/4.0) if a * x < 0 else sin(x) - b**2

a, b, x = map(float, input().split())

print(find_y(a, b, x))
