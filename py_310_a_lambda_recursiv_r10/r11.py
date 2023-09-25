# R 11:

# Qiymat qaytaradigan funksiya e'lon qiling va u parametr sifatida n qabul
# qilsin va u o'zida list qabul qilib, list elementlari yig'indisini  nga
# ko'paytiriib qaytaradigan lambda functionni return qilsin.

def som(n: int) -> int():
    """
    som'dagi qiymatni lamdadagi list'ning yig'indisiga ko'parytirib beradi
    """
    return lambda lst: sum(lst) * n


lst = [2, 3, 4, 5]
n = 2
sup = som(n)
print(sup(lst))
