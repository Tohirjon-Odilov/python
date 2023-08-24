# P19:

# Ikkita butun sonlardan iborat listlar berilgan.
# Ushbu ikkita listlarda ikkalasida ham uchraydigan sonlarni
# new nomli listga joylashtiring.
# Input:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# Output: new=[1, 2, 3, 4, 5, 8, 13]

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 1, 2, 23]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = list()

if len(a) < len(b):
    for i in b:
        if i in a:
            c.append(i)
if len(a) >= len(b):
    for i in a:
        if i in b:
            c.append(i)
print(c)
