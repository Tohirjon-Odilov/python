# P9:

# Foydalanuvchi list kiritadi. Shu listdagi 2 chi eng katta qiymatni toping:

# Input:       [2, 1, -4, -9, 0, -5, 8, 3]
# Output:    3

lst = [2, 1, -4, -9, 0, -5, 8, 3]
# variant 0
# lst.sort(reverse=True)
# print(lst[1])

# update and variant 1
print(sorted(lst, reverse=True)[1])

# variant 2
# lst.remove(max(lst))
# print(max(lst))
