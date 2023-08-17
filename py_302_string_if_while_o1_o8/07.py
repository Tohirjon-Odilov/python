def tub(number):
    if number <= 2:
        return True if number == 2 else False

    if number % 2 == 0:
        return False

    i = 3
    while i*i <= number:
        if number % i == 0:
            return False
        i += 2

    return True

def teskari_tub(number):
    if number < 10:
        return False
    else:
        number = (number % 10) * 10 + (number // 10)

    if number <= 2:
        return True if number == 2 else False

    if number % 2 == 0:
        return False

    i = 3
    while i*i <= number:
        if number % i == 0:
            return False
        i += 2

    return True


i = 1
while i < 100:
    a = teskari_tub(i)
    if a and tub(i):
        print(i, "<--->", str(i)[::-1])
    i += 1

# num, i = 20, 1
# j = 0
# isTrue = True
# while i <= num:
    # l = 2
    # if i <= 2:
    #     isTrue = True if i == 2 else False
    # while l < i:
    #     if i % l == 0:
    #         isTrue = False
    #         break
    #     l += 1
    # if isTrue and i == 2:
    #     print(i)
    # elif isTrue:
    #     print(i)
    #     isTrue = True
        # isTrue = False
    # j = 0
    # i += 1

# if number <= 2:
#     return True if number == 2 else False

# if number % 2 == 0:
#     return False

# i = 3
# while i*i <= number:
#     if number % i == 0:
#         return False
#     i+=2

# return True
