# Q8:

rim_nums = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX",
    10: "X",
    40: "XL",
    50: "L",
    90: "XC",
    100: "C",
    400: "CD",
    500: "D",
    900: "CM",
    1000: "M"
}

# num = int(input("Son kiriting: "))
num = int(str(10)[::-1])
# LVIII
i = 1
while 0 < num:
    rim = num % 10 * i
    # print(rim, end="")
    # if rim <= 10:
        # while num > 5:
            # if
            # num -= 1
    if rim in rim_nums:
        print(rim_nums[rim], end="")
    num //= 10
    i *= 10
# print(rim_nums)
