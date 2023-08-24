# R8:

# Function tuzing. Bu function natural sonlardan iborat list qabul qiladi. Va
# shu sonlardan yasash mumkin bo'lsan eng katta qiymatni qaytaradi:

# Input:     [1, 2, 3]
# Output: 321

# ———————————————————

# Input:    [61, 228, 9]
# Output: 961228


def cat(lst: list) -> int():
    num_str = list(map(int, map(lambda a: str(a)[0], lst)))
    num = list(map(str, lst))
    txt = str()
    # n = int()
    # print(list(map()))
    num_str.sort(reverse=True)
    num_str = list(map(str, num_str))
    for el in num_str:
        for j in num:
            if el == j[0]:
                # n = j[0]
                txt += j
                break
    txt = int(txt)
    return txt


lst = [61, 228, 9]
# lst = [1, 2, 3, 4]

print(cat(lst))
