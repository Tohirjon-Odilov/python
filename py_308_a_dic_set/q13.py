# Q 13:

# User ma'lumot kiritadi va siz bu ma'lumotni dictionaryga qo'shib borasiz.
# Keylar esa 1 Dan boshlab o'sish tartibida bo'ladi.

# Qachinki user,  exit so'zini kiritsa, ma'lumot qo'shish to'xtaydi va
# ekranga barcha ma'lumotlar chiqarib beriladi.
thisdict = {}
n = str()
count = 1
while True:
    n = input("Nimadir yozing: ")
    if n == "exit":
        break
    thisdict.update({count: n})
    count += 1
print(thisdict)
