# T1:
# Erkaklarni ismi, familiyasi, davlatini chop eting
if 0:
    file = open("people_count.txt", "r")
    data = file.read()
    data = data.split("\n")
    for i in range(len(data)):
        data[i] = data[i].split(",")

    data.pop()

    for i in range(len(data)):
        data[i][3] = int(data[i][3])

    for i in data:
        if i[2] == "Male":
            print(i[0].center(10, "-"), i[1].center(10, "-"), i[4].center(10, "-"))

    file.close()
    format(100000, ",")

if 1:
    """
    T2:

    1 - shahar nomi
    2 - aholi soni
    3 - tili

    1. Aholi soni 1 mln dan kop bo'lgan ma'lumotlarni ekranga chiqaring.
    """
    file = open("languages.txt", "r", encoding="utf-8")
    data = file.read().split("\n")[:-1]
    data = list(map(lambda a: a.split(","), data))
    data = list(filter(lambda a: 1000000 <= int(a[1]), data))
    for i, el in enumerate(data, 1):
        print(i, el)
    file.close()
