# R5:

# List ichidagi har bir tuple qiymatlarinig yig'indisini yangi listga
# joylashtiradigan funksiya yozing.

# Input:     [(1, 2), (2, 3), (3, 4)]
# Output:  [3, 5, 7]

# —————————————————————————

# Input:      [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
# Output:   [9, -1, 7, 8]

def sum_list(lst: list()):
    summ = list(map(sum, lst))
    return summ


# lst = [(1, 2), (2, 3), (3, 4)]
lst = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
print(sum_list(lst))
