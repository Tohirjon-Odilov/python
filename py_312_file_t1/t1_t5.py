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
        # for i in data:
        #     if i[-1] == "false" and 1000 > float(i[-2][1:]):
        #         print(i[2])
        data = list(
            filter(
                lambda line: float(line[-2][1:]) > 1000 and line[-1] == "false", data
            )
        )
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
        times = int(input("Soatni kiriting: "))
        for i in data:
            n = i[-1][:2].replace(":", "")
            if times <= int(n):
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
            if 12 <= n <= 20 and country.upper() == i[1]:
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
if 0:
    # T6 ########
    # Foydalanuvchi ismlarni kiritadi sizning vazifangiz barcha kiritilgan ismlarni faylga alohida
    # qatorlarga yozib qo'yish. Foydalanuvchi qachonki stop so'zini kiritsa, ma'lumot qabul qilish
    # to'xtatilsin.
    file = open("names.txt", "a")
    name = str()
    while name != "stop":
        name = input("Enter names: ")
        data = file.write(name + "\n")
    file.close()
if 0:
    # T7:

    # Foydalanuvchi har xil so'zlarni kiritadi va sizning vazifangiz faylga shu so'zlarni saqlash.
    # So'zlarni kiritib bergach foydalanuvchi bir string kiritadi va siz fayl ichidagi ma'lumotlardan
    # kiritilgan stringga o'xshash so'zlarni chiqarish.

    # Masalan ab deg kiritsa, abo, sabab, beadab so'zi ham chiqishi kerak.
    file = open("sentence.txt", "a+")
    while True:
        sentense = input("So'z kiriting: ")
        if sentense.lower() == "stop":
            break
        file.write(sentense + " ")
    file.seek(0)
    data = file.read()
    file.close()
    data = data.split()
    txt = input("Enter sentence: ")
    for i in data:
        if i.find(txt) != -1:
            print(i)
if 0:
    # T8:

    # Fayl ichidagi betartib berilgan raqamlarni boshqa faylga tartiblangan tarzda yozing.
    # Ya'ni bir qatorda bitta raqam holatiga keltirishingiz kerak.

    file = open("raqamlar.txt", "r")
    data = file.read().split("+")
    wrote = open("telphone.txt", "w")
    for _, i in enumerate(data):
        if _ == 0:
            continue
        wrote.write("+" + i + "\n")
    wrote.close()
    file.close()

if 1:
    from time import sleep
    from sys import *

    # import os
    from os import system
    from myfunction import *

    """
    T 9:
    Dastur ishga tushgan vaqtda ekranga 2ta variant chiqsin.
    1. Kompaniya bo'yicha qidirish.
    2. Qolip bo'yicha bo'yicha qidirish

    Kompaniya bo'yicha qidirish tanlansa ekranga
    1. Beeline
    2. Uzmobile
    3. MobiUz
    4. Humans

    chiqsin.

    Kompaniyalarning biri tanlangach shu kompaniyalarga tegishli kodlar
    (90/91...) lar ro'yaxti chiqsin.

    kodni tanlagach shu kod bilan boshlanuvchi 15 ta raqam va ro'yxat agar yana
    raqamlar bo'sa  16. Yana ko'rsatish  menyusi ham qo'shilib qolsin, aks
    xolda chiqmasin.

    Kerakli raqam tanlangach,"Rostdan ham shu raqamni sotib olmoqchimisiz?"
    degan yozuv chiqsin va sotilib olishni tanlasa tanlangan raqamni filedan
    o'chirib tashlasin va soldNumbers.txtga sotilgan raqamni kiritib qo'ysin
    "Xaridingiz uchun rahmat" degan yozuv chiqsin.
    """
    with open("telphone.txt", "r") as file:
        system("clear")
        data = file.readlines()
        data = list(map(lambda line: line[:-1], data))
        print("1. Kompaniya bo'yicha qidirish.\n2. Qolip bo'yicha bo'yicha qidirish.")
        try:
            selected_menu = int(input("<<1>> yoki <<2>> ni kiriting.\n>>> ").strip())

            if selected_menu == 1:
                system("clear")
                print("Qaysi kompaniya kerak:")
                print(
                    "1. Beeline\n2. Uzmobile\n3. MobiUz\n4. Humans\n5. Ucell (Hoyotning yorqin tarafida bo'l!!!)"
                )
                selected_company = int(input("\nTepadagidan birini tanlang.\n>>> "))
                system("clear")
                if selected_company == 1:
                    print("Siz Beelin'ni tanladingiz.\n\n<<90>>\n<<91>>\n")
                    selected_company_code = input("Nechchiligi kerak: ")
                    print("+------+--------------------+")
                    if selected_company_code == "90" or selected_company_code == "91":
                        select_number(data, selected_company_code, 0, 15)
                    else:
                        print("Siz noto'g'ri kod kiritdingiz. Qaytadan urinib ko'ring.")
                elif selected_company == 2:
                    print("<<95>>\n<<99>>")
                    selected_company_code = input("Nechchiligi kerak: ")
                    print("+------+--------------------+")
                    if selected_company_code == "95" or selected_company_code == "99":
                        select_number(data, selected_company_code, 0, 15)
                    else:
                        print(
                            "Siz noto'g'ri kod' kiritdingiz. Qaytadan urinib ko'ring."
                        )
                elif selected_company == 3:
                    print("Faqatgina <<97>> kodligi mavjud!")
                    sleep(2)
                    print("+------+--------------------+")
                    select_number(data, "97", 0, 15)
                elif selected_company == 4:
                    print("<<92>>\n<<96>>")
                    selected_company_code = input("Nechchiligi kerak: ")
                    print("+------+--------------------+")
                    if selected_company_code == "92" or selected_company_code == "96":
                        select_number(data, selected_company_code, 0, 15)
                    else:
                        print(
                            "Siz noto'g'ri kod' kiritdingiz. Qaytadan urinib ko'ring."
                        )
                elif selected_company == 5:
                    print("<<93>>\n<<94>>")
                    selected_company_code = input("Nechchiligi kerak: ")
                    print("+------+--------------------+")
                    if selected_company_code == "93" or selected_company_code == "94":
                        select_number(data, selected_company_code, 0, 15)
                    else:
                        exit("Siz noto'g'ri kod' kiritdingiz. Qaytadan urinib ko'ring.")
            elif selected_menu == 2:
                while True:
                    system("clear")
                    print("Taxminiy raqam kiriting.\nMasalan: 90 123 45 67")
                    searched_number = input(
                        ">>> ",
                    ).strip()
                    if " " in searched_number or len(searched_number) == 3 or 2:
                        serched_number_to_list(data, searched_number, [15, "salom"])
                        exit("\033[1;31mDastur to'xtadi\033[1;0m")
                    else:
                        sleep(1)
                        print(
                            "Siz noto'g'ri formatda kiritdingiz. Qaytadan urinib ko'ring."
                        )
                        continue
            else:
                exit(
                    "\nKo'rsatilgan raqamlardan boshqasi kiritildi.\n\033[1;31mDastur to'xtadi!"
                )
        except Exception as e:
            exit("\n" + e + "\n" + "\n\033[1;31mDastur to'xtadi.")
        except KeyboardInterrupt:
            exit("\033[1;31m\nDastur to'xtadi!")

if 0:
    txt = "Test sinovlarida natijangiz pastroq bo'lsa, bundan tushkunlikka tushmang."
    first = list(txt.split()[0])
    first.reverse()
    last = list(txt.split()[-1])
    last.reverse()
    txt = ["".join(first)] + txt.split()[1:-1] + ["".join(last)]
    print(" ".join(txt))
