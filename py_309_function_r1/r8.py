# R8:

# Function tuzing. Bu function natural sonlardan iborat list qabul qiladi. Va
# shu sonlardan yasash mumkin bo'lsan eng katta qiymatni qaytaradi:

# Input:     [1, 2, 3]
# Output: 321

# ———————————————————

# Input:    [61, 228, 9]
# Output: 961228


def cat(lst: list) -> int():
    num = list(map(str, lst))
    num_str = list(map(lambda a: a[0], num))
    txt = str()

    num_str.sort(reverse=True)
    for el in num_str:
        for j in num:
            if el == j[0]:
                txt += j
                break
    return int(txt)


lst = [61, 288, 9, 78, 43, 55]
# lst = [1, 2, 3, 4]

print(cat(lst))
