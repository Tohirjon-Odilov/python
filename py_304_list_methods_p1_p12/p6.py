# P6:

# Rasmdagi kabi ichma ich list berilgan. Siz esa, qaysi qatordagi elementlar
# yig'indisi eng katta bo'lsa o'sha yig'indini chiqaring.

# Output: 16     (chunki 2+8+6=16)

numbers = [
    [5, 3, 7],
    [5, 9, 6],
    [9, 7, 1],
]

# max_sum = 0
# for i in range(len(numbers)):
#     summ = sum(numbers[i])
#     if summ > max_sum:
#         max_sum = summ

# print(max_sum)

# update
max_sum = 0
for i in range(len(numbers)):
    if sum(numbers[i]) > max_sum:
        max_sum = sum(numbers[i])
print(max_sum)
