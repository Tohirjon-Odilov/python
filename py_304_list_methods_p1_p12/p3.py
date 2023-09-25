"""P3:

Barcha nol raqamlarni listning oxiriga o‘tkazing.

Input:
[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9 ,
 7, 1]

Output:
[3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0 ,
 0, 0]
"""

lst = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2,
       9, 7, 1]
print(lst)
lst3 = list()
count = 0
for i in range(len(lst)):
    if lst[i] == 0:
        count += 1
        continue
    lst3.append(lst[i])

lst3.extend([0] * count)

print(lst3)
