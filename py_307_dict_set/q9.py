# Q9:

# User tomonidan ma'lumotlar kiritiladi va setga joylab boriladi. Sizning
# vazifangiz, avval kiritilgan ma'lumot kiritilsa, ma'lumot kiritilishi
# tugatilsin va ekranga barcha kiritilgan ma'lumotlarni 2lantirib (2ga
# ko'paytirib chiqarilsin.

# Element bor yo'qligini tekshirishda hech qanday looplardan foydalanilmasin.

isDuble = True
thisset = set()
count = 0
n = None
while isDuble:
    n = int(input("Son kiriting: "))
    thisset.add(n)
    count += 1
    if len(thisset) != count:
        isDuble = False
thisset.remove(n)
thisset.add(n*2)
print(thisset)
