# R 15:

# User o'zi istagancha raqam kiritadi, sizning vazifangiz ularni 10dan
# kattalarini o'rnida True, boshqalarini o'rniga esa False qo'yib  return
# qiladigan function yozing.

def nums() -> list():
    lst, bol, isEnter = list(), list(), True
    while isEnter:
        n = input("Nuqta stop!!!\nSon kiriting: ")
        if n == '.':
            isEnter = False
            return bol
        lst.append(n)
        bol = list(map(lambda n: int(n) > 10, lst))
    return bol


print(nums())
