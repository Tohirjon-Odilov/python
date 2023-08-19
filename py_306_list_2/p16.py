# P16:
# Belgilangan List raqamlarini undan juft raqamlarni olib tashlagandan
# so'ng chop etish uchun Python dasturini yozing.

# Namuna roʻyxati :  lst = [23, 44, 56, 99, 111, 23, 54]
# Kutilayotgan natija: [23, 99, 111, 23]

lst = [23, 44, 56, 99, 111, 23, 54]
lst1 = list()
for el in lst:
    if el % 2:
        lst1.append(el)
lst = lst1
print(lst)
