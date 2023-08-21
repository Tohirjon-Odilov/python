# P21:

# Sizga faqat raqamlardan iborat list beriladi siz uni raqamga o'girib birni
# qoshib list qilib qaytarishingiz kerak,

# Input:     [1,2,3]
# Output: [1,2,4]
# Tushuntirish: 123 ga birni qoshilsa 124 va siz [1,2,4] qilib qaytarishingiz
# kerak

# Input      [9]
# Output: [1,0]

# Input:     [9,9,9,9]
# Output: [1,0,0,0,0]

# lst1 = [1, 2, 3]
# lst1 = [9, 9, 9, 9]
lst1 = [9]

lst1 = map(str, lst1)
lst_to_str = str()

for i in lst1:
    lst_to_str += i
lst_to_str = list(tuple(str(int(lst_to_str) + 1)))

for i, el in enumerate(lst_to_str):
    lst_to_str[i] = int(el)
print(lst_to_str)
