# P14:

# List ichidagi elementlarni palindromligini aniqlaydigan dastur tuzing.
#   ["ada", 212, False, 4567, "aziza"]
#   ada - > palindrom
#   212 - > palindrom
#   False - > palindrom emas
#   4567 - > palindrom emas
#   'aziza' - > palindrom

lst = ["ada", 212, False, 4567, "aziza"]

for i in lst:
    i = str(i)
    # print(lst[i][::-1])
    if i == i[::-1]:
        print(i, "-> palindrom")
    else:
        print(i, "-> palindrom emas")
