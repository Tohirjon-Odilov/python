# P8:

# Berilgan listga 6000 dan keyin 7000 ni qo'shib qo'ying (xuddi rasmdagidek)..

list1 = [10, 20, [300, 400, 6000, [5000, 6000], 500], 6000]

for i in range(len(list1)):
    if 6000 == list1[i]:
        list1.insert(i+1, 7000)
    if type(list1[i]) == list:
        for j in range(len(list1[i])):
            if 6000 == list1[i][j]:
                list1[i].insert(j+1, 7000)
            if type(list1[i][j]) == list:
                for m in range(len(list1[i][j])):
                    if 6000 == list1[i][j][m]:
                        list1[i][j].insert(m+1, 7000)
print(list1)
