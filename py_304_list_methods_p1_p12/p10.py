# P10:

# Berilgan listni shunday yangilangki, qiymatlar takrorlanmasin

# Input:        [2, 5, 1, 4, 3, 2, 1, 6, 8, 5, 7, 9]
# Output:     [2, 5, 1, 4, 3, 6, 8, 7, 9]

list1 = [2, 5, 1, 4, 3, 2, 1, 6, 8, 5, 7, 9]
list2 = list()

for i in range(len(list1)):
    if not (list1[i] in list2):
        list2.append(list1[i])

list1 = list2
print(list1)
