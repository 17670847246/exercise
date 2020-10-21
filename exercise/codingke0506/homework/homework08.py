# def gcd(x, y):
#     x, y = (y , x) if x > y else (x, y)
#     for i in range(x, 0, -1):
#         if x % i == 0 and y % i == 0:
#             return i

def gcd(x, y):
    while y % x != 0:
        x, y = y % x, x
    return x


# 27 15 ---> 12 15 ---> 3 12 ---> 3
print(gcd(27, 15))
print(gcd(24, 72))
print(gcd(22, 88))
