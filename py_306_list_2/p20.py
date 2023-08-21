# P20:

# Berilgan ro'yxatda elementlarni o'sish , kamayish yoki tartibsiz joylashgani
# ni aniqlovchi dastur tuzing.

# Input: [5,3,8,1]
# Output: tartibsiz

# Input: [1,4,7,9]
# Output: o'sis

# lst1 = [5, 3, 8, 1]
# lst1 = [1, 4, 7, 9]
lst1 = [9, 8, 5, 3]

if lst1 == sorted(lst1):
    print("o'sish")
elif lst1 == sorted(lst1, reverse=True):
    print("kamayish")
else:
    print("tartibsiz")
