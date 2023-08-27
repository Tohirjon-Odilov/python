birliklar = ["", "bir", "ikki", "uch", "to'rt", "besh", "olti", "yetti", "sakkiz", "to'qqiz"]
onliklar = ["", "o'n", "yigirma", "o'ttiz", "qirq", "ellik", "oltmish", "yetmish", "sakson", "to'qson"]
yuzlar = ["", "bir yuz", "ikki yuz", "uch yuz", "to'rt yuz", "besh yuz", "olti yuz", "yetti yuz", "sakkiz yuz", "to'qqiz yuz"]

def sonni_oqiyapman(son):
    yuz_miqdori = son // 100
    onlik_miqdori = (son % 100) // 10
    birlik_miqdori = son % 10

    natija = ""
    if yuz_miqdori > 0:
        natija += yuzlar[yuz_miqdori] + " "
    if onlik_miqdori > 0:
        natija += onliklar[onlik_miqdori] + " "
    if birlik_miqdori > 0:
        natija += birliklar[birlik_miqdori]

    return natija

son = int(input("Istalgan sonni kiriting (1 dan 1000 gacha): "))
if son < 1 or son > 1000000000:
    print("Noto'g'ri kirish! Faqat 1 dan 1000 gacha bo'lgan son kiriting.")
else:
    natija = sonni_oqiyapman(son)
    print("Natija:", natija)
