# R3:

# a dan b gacha sonlarni ekranga chiqaradigan recursive function tuzing.
# Faqat, a >= b dan bo'lgan holatlar uchun

# Input:    7 2
# Output: 7 6 4 5 3 2

# def rev(a: int, b: int):
#     if a >= b:
#         print(a)
#         rev(a-1, b)


# rev(7, 2)


# R4:

# # Function tuzing. String qabul qilsin. Katta harflar sonini va kichik
# # harflarni sonini qaytarsin.

# # Input:     "Good Luck"
# # Output:  [2, 6]

# def countstr(txt):
#     upper = int()
#     lower = int()

#     for i in txt:
#         if i.islower():
#             lower += 1
#         elif i.isupper():
#             upper += 1
#     return upper, lower


# txt = "Good Luck"
# str = list(countstr(txt))
# print(str)


# R5:

# # List ichidagi har bir tuple qiymatlarinig yig'indisini yangi listga
# # joylashtiradigan funksiya yozing.

# # Input:     [(1, 2), (2, 3), (3, 4)]
# # Output:  [3, 5, 7]

# # —————————————————————————

# # Input:      [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
# # Output:   [9, -1, 7, 8]

# def sum_list(lst: list()):
#     summ = list(map(sum, lst))
#     return summ


# # lst = [(1, 2), (2, 3), (3, 4)]
# lst = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
# print(sum_list(lst))


# R6:

# # Function tuzing. Bu function, listning ichidagi tuple ni listga o'girib
# # bersin.

# # Input:     [(1, 2), (2, 3), (3, 4)]
# # Output:  [[1, 2], [2, 3], [3, 4]]

# # —————————————————————————

# # Input:     [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
# # Output:  [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]

# def tuple_to_list(lst: list()):
#     return list(map(list, lst))


# # lst = [(1, 2), (2, 3), (3, 4)]
# lst = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
# lst = tuple_to_list(lst)
# print(lst)


# R7:

# # Uchta list ni quyidagicha birlashtiruvchi function tuzing:

# # Input:
# # ['S001', 'S002', 'S003', 'S004']
# # ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# # [85, 98, 89, 92]

# # Output:
# # [
# #      {'S001': {'Adina Park': 85}},
# #      {'S002': {'Leyton Marsh': 98}},
# #      {'S003': {'Duncan Boyle': 89}},
# #      {'S004': {'Saim Richards': 92}}
# # ]

# # Note: natijada list ichida dictionary lar xosil bo'lgan
# thisdict = dict()
# thislist = list()


# def format_list(nums: list, names: list, ages: list) -> list():
#     for i in range(len(nums)):
#         thisdict[nums[i]] = {names[i]: ages[i]}
#     for i in thisdict.items():
#         thislist.append({i[0]: i[1]})


# nums = ['S001', 'S002', 'S003', 'S004']
# names = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# ages = [85, 98, 89, 92]

# format_list(nums, names, ages)
# print(thislist)


# R8:

# # Function tuzing. Bu function natural sonlardan iborat list qabul qiladi. Va
# # shu sonlardan yasash mumkin bo'lsan eng katta qiymatni qaytaradi:

# # Input:     [1, 2, 3]
# # Output: 321

# # ———————————————————

# # Input:    [61, 228, 9]
# # Output: 961228


# def cat(lst: list) -> int():
#     num = list(map(str, lst))
#     num_str = list(map(lambda a: a[0], num))
#     txt = str()

#     num_str.sort(reverse=True)
#     for el in num_str:
#         for j in num:
#             if el == j[0]:
#                 txt += j
#                 break
#     return int(txt)


# lst = [61, 288, 9, 78, 43, 55]
# # lst = [1, 2, 3, 4]

# print(cat(lst))


# R9:

# # Ichma ich list qabul qiluvchi va quyidagicha dictionary qaytaruvchi
# # function tuzing

# # Input:
# # [
# #       [1, 'Jean Castro', 'V'],
# #       [2, 'Lula Powell', 'V'],
# #       [3, 'Brian Howell', 'VI'],
# #       [4, 'Lynne Foster', 'VI'],
# #       [5, 'Zachary Simon', 'VII']
# # ]

# # Output:
# # {
# #      1: ['Jean Castro', 'V'],
# #      2: ['Lula Powell', 'V'],
# #      3: ['Brian Howell', 'VI'],
# #      4: ['Lynne Foster', 'VI'],
# #      5: ['Zachary Simon', 'VII']
# # }

# def format_to_dict(lst: list) -> list():
#     thisdict = dict()
#     i = 0
#     while i in range(len(lst)):
#         del lst[i][0]
#         i += 1
#     for i, el in enumerate(lst):
#         thisdict[i+1] = el
#     return thisdict


# lst = [[1, 'Jean Castro', 'V'],
#        [2, 'Lula Powell', 'V'],
#        [3, 'Brian Howell', 'VI'],
#        [4, 'Lynne Foster', 'VI'],
#        [5, 'Zachary Simon', 'VII']
#        ]


# print(format_to_dict(lst))
