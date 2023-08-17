# num, i = 100, 0

# while i <= 100:
#     if str(i).find('3') != -1:
#         print(i, end=" ")
#     i += 1

# update
count = 0
for i in range(1, 101):
    if 3 in i:
        count += 1
        print(i)
