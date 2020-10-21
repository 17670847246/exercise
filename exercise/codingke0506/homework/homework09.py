def is_prime(num):
    for factor in range(2, int(num ** 0.5) + 1):
        if num % factor == 0:
            return False
    return num != 1

# 60 = 1 2 3 4 5 6 10 12 15 20 30 60

#
# list1 = []
# for n in range(2, 100):
#     if is_prime(n):
#         list1.append(n)
# print(list1)