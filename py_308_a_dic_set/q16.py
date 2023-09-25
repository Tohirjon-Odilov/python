# Q 16:

# User avvalo n ni kiritadi va sizning vazifangiz dictionaryga n ta ma'lumot
# qo'shish.

# Buning uchun avval user keyni (o'zbekcha so'z) va keyin valueni (inglizcha
# so'z) kiritadi.

# Ma'lumotlar soni nga yetganda ma'lumot qo'shish to'xtaydi.

# Keyin ekranga so'zni kiriting degan ma'lumot chiqadi va user istasa
# inglizcha, istasa o'zbekcha so'z kiritadi, sizning vazifangiz o'sha so'z va
# uning tarjimasini chiqarish.

# Agar kiritilgan so'z mavjud bo'lmasa bunday so'z mavjud emas desin.

n = int(input("Son kiriting: "))
thisdict = dict({"book": 'kitob', "pen": "ruchka", "pencil": "qalam",
                 "hello": "salom"})
while n:
    thisdict.update({input("\nEnglish: "): input("\nUzbek: ")})
    print("="*20)
    n -= 1
find_text = input("So'zni kiriting: ")
check = True
for i, j in thisdict.items():
    if i == find_text or j == find_text:
        print(i, "=>", j)
        check = False
if check:
    print("Bunday so'z mavjud emas!")
# if thisdict.values(find_text):
#     print(thisdict.get(find_text))
# elif find_text in thisdict.values():
#     for i in thisdict.values():


# print(thisdict.values())
