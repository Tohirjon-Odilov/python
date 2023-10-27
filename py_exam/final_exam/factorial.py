def factorial(num):
    nums = 1
    for i in range(1, num+1):
        nums *= i
    return nums

def factorial_num(num: int) -> int:
    count = 1
    while True:
        if num == factorial(count):
           return count
        elif num < factorial(count):
            return "Number is not a factorial!"
        count += 1

print(factorial_num(1307674368000))