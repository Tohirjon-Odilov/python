# lst = []

# for i in range(5):
#     lst.append(i)
# lst.reverse()
# print(lst)
# list.insert(8, 49)

list = [True, "Salom", 5, 5.6]

for i in range(len(list)):  # 4
    list[i] = type(list[i])
print(list)
