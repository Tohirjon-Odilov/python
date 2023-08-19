# P12:

# Ikkita listning o'rta arifmetigini chiqaring.

# Input:
# [1, 1, 3, 4, 4, 5, 6, 7]
# [0, 1, 2, 3, 4, 4, 5, 7, 8]

# Output:
# 3.823529411764706

list1 = [1, 1, 3, 4, 4, 5, 6, 7]
list2 = [0, 1, 2, 3, 4, 4, 5, 7, 8]

# count = 0
# summ = sum(list2) + sum(list1)

# for i in list1:
#     count += 1
# for i in list2:
#     count += 1

# print(summ / count)

# upgrade
list1 += list2
print(sum(list1) / len(list1))
