# Q10:

# 2 ta ichida 5 tasan elementi bor setlar berilgan, sizning vazifangiz ikkita
# setning bir-birida mavjud bo'lmagan ma'lumotlari bir listga va o'xshash
# elementlarini boshqa listga qo'shib, ikkala list elementlari yig'indisidan
# hosil bo'lgan raqamlarni ayirmasini topish.

lst1 = {1, 5, 6, 9, 5, 8}
lst2 = {2, 5, 6, 8, -5, 10}

dif = lst1.difference(lst2)
intr = lst1.intersection(lst2)
print(sum(intr)-sum(dif))
