# def is_panlindrome(num):
#     return str(num) == str(num)[::-1]
#
# print(is_panlindrome(123432))

# 12321 --> 1, 1232 --> 12, 123 --> 123, 12 ---> 1232, 1 --> 12321, 0

def is_palindrome(num):
    total, temp =0, num
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num

# print(is_palindrome(23))
# print(is_palindrome(53))
# print(is_palindrome(63))
# print(is_palindrome(12321))