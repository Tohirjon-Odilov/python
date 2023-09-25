# lst = [11,22,33,44,55,66,77,88,99]

# lst.append(100) -> list ga qiymat qo'shadi
# lst.clear() -> lsitni tozalab tashlaydi
# new = lst.copy() -> new ge lst'ni qiymatlarini beradi
# x = lst.count(11) -> listda nechta 11 borligini sanaydi
# lst.extend([22,33]) -> listni echib ichiga solib qoyadi
# lst.append([22,33]) -> listni ochmasdan ichiga solib qoyadi
# lst.insert(2,39) ikkinchi index ga 39 ni qo'shadi
# lst.pop(2) -> 2-indexdagi elementni o'chirib tashlaydi
# lst.pop() -> oxirgi elementli olib tashlaydi
# lst.remove(99) -> listdan berilgan qiymatni olib tashlaydi
# lst.reverse() -> listni teskari qiladi
# lst.sort() -> listni osish tartibida sortlaydi
# del lst -> lst listini ochirib tashlaydi
# del lst[0] -> 0-indexdagi elementni olib tashlaydi
# lst = sorted(lst) -> listni sortlaydi
# print(min(lst)) -> list ichidan minimumini qaytaradi
# print(max(lst)) -> list ichidan maximumini qaytaradi
# print(sum(lst)) -> list ichidagi elementalr yig'indisini qaytaradi
# enumerate() -> index va elementni tuplda qaytaradi
# isinstance(8, int) -> agar 8 ning type == int bo'lsa true qaytaradi

# bir qatorli for va ichida if

# 1-usul
# odd = [i for i in range(5) if i % 2] # 1, 3
# even = [i for i in range(5) if i % 2 == 0] # 0 2 4
# 2-usul
# lst = [i for i in range(5)] # 0, 1, 2, 3, 4
# odd = [num for num in lst if num % 2] # 0, 2, 4
# even = [i for i in lst if i % 2 == 0] # 1, 3
# 3-usul
# lst = [i for i in range(5)] # 0, 1, 2, 3, 4
# odd = []
# even = []
# for i in lst: odd.append(i) if i % 2 else even.append(i)