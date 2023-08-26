# R 10:

# Lambda function e'lon qiling va u o'zida parametr sifatida 2ta list
# qabul qilsin. Sizning vazifangiz, o'sha listlar raqamlari yig'indisining
# ayirmasini ekranga chiqarish.

lst1 = [1, 2, 3, 45, 6]
lst2 = [11, 22, 5, 4, 9]

addaction = lambda a, b: sum(a)-sum(b)

print(addaction(lst1, lst2))
