# R 17:

# User o'zi istagancha son va min,max qiymatlarni kiritadi, sinznig
# vazifangiz min va max oralig'iga tushadigan raqamlar listini return
# qiladigan funksiya yozish.

def duble(lst: list, st: int, sp: int) -> list():
    return list(filter(lambda a: a >= st and a < sp, lst))


mn, mx = int(input("Min son kiriting: ")), int(input("Max son kiriting: "))
isEnter, thislist = True, list()
print('Stop nuqta (.)')
while isEnter:
    n = input("Son kiriting: ")
    if n == ".":
        isEnter = False
        break
    n = int(n)
    thislist.append(n)
print(duble(thislist, mn, mx))
