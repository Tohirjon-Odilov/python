# P2:

# Quyidagi arraydan nusxa oling va olingan nusxani juft indexdagilarni 2 chi da
# rajaga ko'tarib,  toq indexdagilarni kubga ko'tarib nusxalangan arrayga
# o'zlashtirib dastlabki va nusxa olingan arrayni ekranga chiqaring

# input:    [7, 8, 1, 3, 4, 6, 7, 5]
# output: [49, 512, 1, 27, 16, 216, 49, 125]

lst = [7, 8, 1, 3, 4, 6, 7, 5]
print(lst)
lst2 = lst.copy()
for i in range(len(lst2)):
    if i % 2:
        lst2[i] *= lst2[i] * lst2[i]
    else:
        lst2[i] *= lst2[i]

lst = lst2.copy()
print(lst)
