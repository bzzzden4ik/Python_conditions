# 7 вариант
def condition(x, y):
    return ((2 <= x <= 8) and (2 <= y <= 6)) or ((5 <= x <= 8) and (6 <= y <= 8))


x, y = map(float, input().split())

print("TRUE" if condition(x, y) else "FALSE")
