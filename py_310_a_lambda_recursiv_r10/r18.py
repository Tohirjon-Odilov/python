# R 18:

# Elementlari listdan iborat list e'lon qiling.

# Foydalanuvchi min va max qiymatlarni kiritadi.

# Sizning vazifangiz, yuqoridagi listning elementidagi listlarning
# elementlari yig'indisi min va max oraliqqa tushadigan elementlar
# listining yig'indilarini, aks holda o'sha listing birinchi elementini
# qaytaring.


# R 18:

# Elementlari listdan iborat list e'lon qiling.

# Foydalanuvchi min va max qiymatlarni kiritadi.

# Sizning vazifangiz, yuqoridagi listning elementidagi listlarning
# elementlari yig'indisi min va max oraliqqa tushadigan elementlar listini
# qaytaring.

def summ(lst: list, mn: int, mx: int) -> list():
    return list(filter(lambda ll: ll > mn and ll < mx,
                       (list(map(lambda a: sum(a), lst)))))


lst = [[1, 2, 3], [4, 6, 7], [8, 9, 10]]
# lst = [[1, 2], [3, 4], [50, 6]]
mn, mx = int(input("Min sonni kiriting: ")), int(input("Max sonni kiriting: "))
print(summ(lst, mn, mx))
