"""
P4:

Toq indexdagi qiymatlarni kvadratga ko'tarib o'ziga o'zlashtiring
Input:
[
       [2,  15,  4],
       [19, 24, 11],
       [7,   9,  5],
       [10,  3,  1]
]

Output:
[
       [2,  225,  4],
       [19, 576, 11],
       [7,   81,  5],
       [10,   9,  1]
]
"""

lst = [
       [2,  15,  4],
       [19, 24, 11],
       [7,   9,  5],
       [10,  3,  1]
]
print(lst)

for i in range(len(lst)):
    for j in range(len(lst[i])):
        if j % 2:
            pow(lst[i][j], 2)
            # lst[i][j] *= lst[i][j]
print(lst)
