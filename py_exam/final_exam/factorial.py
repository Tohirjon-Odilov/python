def factorial(num):
    i = f = 1
    while f < num:
        i += 1
        f *= i
    if f == num:
        return i
    return "ERROR"

print(factorial(240))


# def factorial(num):
#     nums = 1
#     for i in range(1, num+1):
#         nums *= i
#     return nums

# def factorial_num(num: int) -> int:
#     # print(factorial(5))
#     count = 1
#     while True:
#         if num == factorial(count):
#            return count
#         elif num < factorial(count):
#             return "Number is not a factorial!"
#         count += 1

# print(factorial_num(1307674368000))