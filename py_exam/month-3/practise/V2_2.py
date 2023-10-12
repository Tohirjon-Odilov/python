# Problem 1.
if 0:
    mydict = {1: "salom", 2: 123, 3: "hayr", 4: 456, 5: "alvido"}
    new_dict = {i[0]: i[1] for i in mydict.items() if isinstance(i[1], str)}
    key = dict(sorted(new_dict.items(), key=lambda x: x[1]))
    print(key)
if 0:
    mydict = {1: "salom", 2: 123, 3: "hayr", 4: 456, 5: "alvido"}
    new_dict = {key: value for key, value in mydict.items() if isinstance(value, str)}
    sorted_dict = dict(sorted(new_dict.items(), key=lambda item: item[1]))
    print(sorted_dict)

if 1:

    def yaqin_son_topsish(raqamlar, N):
        yaqin_son = None  # Yaqin sonni o'zgaruvchi sifatida tanlash vaqtincha None
        eng_yaqin_masofa = float(
            "inf"
        )  # Eng yaqin masofani infinitsi yoki chegarasiz sifatida tanlash
        print(eng_yaqin_masofa)
        for raqam in raqamlar:
            masofa = abs(
                raqam - N
            )  # N va listdagi raqam orasidagi masofani hisoblaymiz
            if masofa < eng_yaqin_masofa:
                eng_yaqin_masofa = masofa  # Yangi eng yaqin masofani o'zgartiramiz
                yaqin_son = raqam  # Yangi eng yaqin sonni o'zgartiramiz

        return yaqin_son  # Eng yaqin sonni qaytarish

    # Misol:
    # raqamlar = [4, 7, 10, 11, 12, 17]  # 10
    # raqamlar = [4, 7, 10, 11, 12, 17]  # 7
    # raqamlar = [4, 8, 10, 11, 12, 17]  # 8
    # raqamlar = [4, 9, 10, 11, 12, 17]  # 8
    raqamlar = [-1, 2, 3]  # 8
    N = 0
    natija = yaqin_son_topsish(raqamlar, N)
    print(f"{raqamlar}\n{N} ga eng yaqin son: {natija}")
