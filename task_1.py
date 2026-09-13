import math


# 7 вариант
def find_y(a, b, x):
    if a * x < b:
        return math.exp(-2 * x) + (a**4 + x)**(1/4)
    return math.sin(x) - b**2


a, b, x = map(float, input().split())

print(find_y(a, b, x))
