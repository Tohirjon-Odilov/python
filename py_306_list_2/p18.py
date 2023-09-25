# P18:

# Har xil uzunlikdagi Listlar berilgan va sizning
# vazifangiz ushbu listlarni quyidagi shartlar asosida yangi
# listga birlashtirish. Yangi listga birinchi list1 elementi
# va keyin list2 elementini ketma-ketlikda joylashtiring.
# Input: list1=[1, 2, 3]   list2=[11, 22, 33]
# Output: list3=[1, 11, 2, 22, 3, 33]

# Input: list1=[1, 2, 3, 4, 5]   list2=[11, 22, 33]
# Output: list3=[1, 11, 2, 22, 3, 33, 4, 5]

# Input: list1=[1, 2]   list2=[11, 22, 33, 44, 55]
# Output: list3=[1, 11, 2, 22, 33, 44, 55]

# list1 = [1, 2, 3]
# list2 = [11, 22, 33]
# list1 = [1, 2, 3, 4, 5]
# list2 = [11, 22, 33]
list1 = [1, 2]
list2 = [11, 22, 33, 44, 55]
list3 = list()
count = 0

if len(list1) <= len(list2):
    for i in range(len(list2)):
        if len(list1) > i:
            list3.append(list1[i])
            list3.append(list2[i])
        else:
            list3.append(list2[i])
    count = 1

if len(list1) >= len(list2) and count == 0:
    for i in range(len(list1)):
        if len(list2) > i:
            list3.append(list1[i])
            list3.append(list2[i])
        else:
            list3.append(list1[i])
