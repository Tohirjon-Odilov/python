# P5:

# Quyidagi tuple berilgan.
# numbers = (5, -3, 4, -2, 1, -9, 8, -6, 7, 0, 4)

# Foydalanuvchi kiritgan n son, numbers nomli tuple da mavjud bo'lsa,
# barcha n larni o'chirib qo'ying va numbers ni ekranga chiqaring. Agar
# kiritilgan son, tuple da topilmasa hech narsa o'chirmaysiz

# Input:
# 4

# Outpu:
# (5, -3, -2, 1, -9, 8, -6, 7, 0)

numbers = (5, -3, 4, -2, 1, -9, 8, -6, 7, 0, 4)
numbers_to_list = list(numbers)

n = int(input("Son kiriting: "))

while n in numbers_to_list:
    numbers_to_list.remove(n)
numbers_to_list = tuple(numbers_to_list)
print(numbers_to_list)
