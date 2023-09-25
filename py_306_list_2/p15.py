# P15:

# Satr uzunligi 2 va undan ortiq, birinchi va oxirgi belgilari bir xil
# bo‘lgan satrlar sonini hisoblavchi Python dasturini yozing.
#   Namuna roʻyxati : ['abc', 'xyz', 'bo'lib','aba', '1221']
#   Kutilayotgan natija: 3

lst = ['abc', 'xyz', 'bo\'lib', 'aba', '1221']
j = 0
for i in lst:
    if len(i) > 1 and i[0] == i[-1]:
        j += 1
print(j)
