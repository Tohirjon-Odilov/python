# R 13:

# User avval barcha ismlarni kiritadi, so'ng esa barcha familiyalarni
# kiritadi. Siz esa ism va familiyalarni indexiga qarab, dictionaryga
# o'zlashtirib, return qiladigan funksiya yozing.

def full_name(name: str, second_name: str) -> dict():
    ...


count = 0
is_enter = True
while is_enter:
    name = str()
    if name != ".":
        count += 1
        name = input("Ism kiriting: ")
    while count > 0:
        second_name = input("Familiya kiriting: ")
        count -= 1

    full_name(name, second_name)
