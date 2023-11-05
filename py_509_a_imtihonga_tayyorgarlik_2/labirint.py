def chiqish_mumkinligi(matritsa):
    yuk = len(matritsa)
    eni = len(matritsa[0])

    def labirint_tekshirish(y, x):
        if y < 0 or y >= yuk or x < 0 or x >= eni or matritsa[y][x] == 1:
            return False
        if y == yuk - 1 and x == eni - 1:
            return True

        matritsa[y][x] = 1

        if labirint_tekshirish(y + 1, x) or labirint_tekshirish(y - 1, x) or labirint_tekshirish(y, x + 1) or labirint_tekshirish(y, x - 1):
            return True

        matritsa[y][x] = 0
        return False

    return labirint_tekshirish(0, 0)


labirint1 = [[0, 1, 1, 1, 1, 1, 1], 
             [0, 0, 1, 1, 0, 1, 1], 
             [1, 1, 1, 1, 0, 0, 1],
             [1, 0, 0, 0, 0, 1, 1],
             [1, 1, 1, 1, 1, 0, 0]]

labirint2 = [[0, 1, 1, 1, 1, 1, 1],
             [0, 0, 1, 0, 0, 1, 1],
             [1, 0, 0, 0, 0, 1, 1],
             [1, 1, 0, 1, 0, 0, 1],
             [1, 1, 0, 0, 1, 1, 1]]

natija1 = chiqish_mumkinligi(labirint1.copy())  # labirint1 ni ko'chirib olish uchun .copy() qo'shildi
natija2 = chiqish_mumkinligi(labirint2.copy())  # labirint2 ni ko'chirib olish uchun .copy() qo'shildi

print(natija1)  # True
print(natija2)  # False
