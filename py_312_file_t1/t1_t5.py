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

if 0:
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

if 0:
    """
    T3:

    product_material.txt bazasida sizda

    id - produkt ID raqami
    product - produkt kodi
    material - ishlab chiqarilgan materiali
    price - narxi
    is_available - omborda bor yo'qligi berilgan

    1. Maqasadingiz shu ma'lumotlar orasidan narxi 500 va 1000 dollar orasida bo'lgan va omborda mavjud
     bo'lgan produktlar ID raqami va ishlab chiqarilgan materialini chop etish bo'ladi.

    2. Foydalanuvchi material nomini kiritadi va siz unga barcha omborda hozirda mavjud (true) bo'lgan
    produktlar narxlarini o'sish tartibida chiqarib berishingiz lozim

    3. Omborda mavjud bo'lmagan (ya'ni false bo'lgan)  va narxi 1000 dollardan arzon bo'lgan tovarlarning
    ishlab chiqarilgan materialini ekranga chop eting.
    """
    file = open("product_material.txt")
    data = file.readlines()
    file.close()
    data = list(map(lambda a: a[:-1].split(","), data))
    # 1 - shart
    if 0:
        for i in data:
            if i[-1] == "true" and 500 < float(i[-2][1:]) < 1000:
                print(i[0], i[2])

    # 2 - shart
    if 1:
        data.sort(key=lambda a: float(a[3][1:]))
        n = input("Material nomini kiriting: ").title()
        for i in data:
            if i[2] == n and i[-1] == "true":
                # print(
                #     "%-4s | %-35s | %-8s | %-10s | %-5s"
                #     % (i[0], i[1], i[2], i[3], i[4])
                # )
                print(i[-2])
    # 3 - shart
    if 0:
        for i in data:
            if i[-1] == "false" and 1000 > float(i[-2][1:]):
                print(i[2])
if 0:
    """
    T4:

    cinema.txt faylida quyidagi ma'lumotlar keltirilgan

    id - film ID raqami
    movie - film nomi
    genre - film janri
    year - ishlab chiqarilgan yil
    cinema - kinoteatr adresi
    starts_at - film boshlanish vaqti

    1. Foydalanuvchi taxminiy film ko'rish vaqtini kiritadi. Maqsadingiz kiritilgan
    vaqtdan keyingi hamma filmlar ro'yhatini chop etish.
    Foydalanuvchi faqat soatni kiritadi. Minutlarga e'tibor berish shart emas.
    """
    file = open("cinema.txt", "r")
    data = file.readlines()
    file.close()
    data = list(map(lambda a: a[:-1].split(","), data))
    if 0:
        time = int(input("Soat'ni kiriting: "))
        for i in data:
            n = i[-1][:2].replace(":", "")
            if time <= int(n):
                # print(
                #     "%-4s | %-20s | %-8s | %-4s | %-15s | %-5s"
                #     % (i[0], i[1], i[2], i[3], i[4], i[5])
                # )
                print(i[1])
    """
    2. Foydalanuvchiga 2000 yildan keyin ishlab chiqarilgan va <genre> ichida Comedy
    yoki Drama yoki Romance bo'lgan filmlar nomlari va kinoteatr adreslarini chop etib
    bering.
    """
    if 0:
        for i in data:
            if int(i[3]) > 2000 and (
                i[2].find("Romance") != -1
                or i[2].find("Drama") != -1
                or i[2].find("Comedy") != -1
            ):
                print("%-4s | %-40s | %-15s" % (i[3], i[1], i[-2]))
    """
    3. Soat 17:00 dan keyingi barcha Horror filmlar ro'yhatini chop eting.
    """
    if 1:
        for i in data:
            n = int(i[-1][:2].replace(":", ""))
            # if 17 < n and i[2] in "Horror":
            #     print("%-8s %-30s %-30s" % (i[-1], i[2], i[1]))
            if 17 < n and i[2].find("Horror") != -1:
                print("%-8s %-30s %-30s" % (i[-1], i[2], i[1]))
if 0:
    """
    T5:

    booking_data.txt faylida quyidagi ma'lumotlar keltirilgan

    id - ID raqami
    departure - uchib ketish davlati
    d_time - uchish vaqti
    arrive - qo'nish davlati
    a_time - qo'nish vaqti
    cost - bilet narxi

    1. Foydalanuvchi o'zida bor taxminiy pul miqdorini kiritadi. Maqsadingiz shu kiritlgan summadan $50
    arzonroq va $100 qimmatroq bo'lgan biletlar ro'yhatini ko'rsatish
    """
    file = open("booking_data.txt")
    data = file.readlines()
    file.close()
    data = list(map(lambda a: a[:-1].split(","), data))
    if 0:
        price = int(input("Narx kiriting: "))
        for i in data:
            n = float(i[-1][1:])
            if price - 50 < n < price + 100:
                print(
                    "%3s | %5s | %-3s | %-5s | %-10s" % (i[1], i[2], i[3], i[4], i[5])
                )
    """
    2. Kiritilgan davlat bo'yicha barcha aviareyslarni toping. Lekin chiqishda faqat soat 12:00dan
    21:00gacha bo'lgan reyslar chiqsin.
    """
    if 0:
        country = input("Davlat nomini kiriting: ")
        for i in data:
            n = int(i[2][:2].replace(":", ""))
            if 12 <= n <= 21 and country.upper() == i[1]:
                print(
                    "%3s | %5s | %-3s | %-5s | %-10s" % (i[1], i[2], i[3], i[4], i[5])
                )
    """
    3. Tasavvur qiling foydalanuvchi boshqa shahardan uchib kelmoq Lekin u shunday bir qiziq shartni
    aytadi:
    - Men US davlatiga uchishim kerak. Meni har kuni soat 21:00da Zoomda meetingim bo'ladi. Shunga menga
    shunday reys tanlab beringki, qo'nish vaqti meetingdan kamida 1 soat oldin bo'lsin. Menga shu
    reyslarning barchasini ko'rsatsangiz, uchish vaqti qiziq emas.

    Shu shartlarga javob beruvchi barcha reyslarni toping.
    """
    if 1:
        for i in data:
            n = int(i[-2][:2].replace(":", ""))
            if i[3] == "US" and n < 20:
                print(i)
