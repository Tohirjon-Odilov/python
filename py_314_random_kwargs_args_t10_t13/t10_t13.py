""""
T10:

Foydalanuvchi gap kiritadi kiritgan gapni ekranga chop eting. 5 ta taqiqlanuvchi so’zlar mavjud agar foydalanuvchi shu
sozlardan foydalangan bo’lsa shu so’z uzunligicha ‘*’ belgisini ekranga chop eting.
Masalan:
Taqiqlanuvchi so’zlar: [“salom”, “eshmat”, “toshmat”, “dunyo”, “noutbuk”]
input: “SaloM do’stim eshmat bugun men yangi noutbuk sotib oldim”
output: “***** do’stim ****** bugun men yangi ******* sotib oldim
"""
if 0:
    words = ["salom", "eshmat", "toshmat", "dunyo", "noutbuk"]
    input_str = input("Enter a sentence: ")
    for input_word in input_str.split():
        if input_word.lower() in words:
            print("*" * len(input_word), end=" ")
            continue
        print(input_word, end=" ")
"""
T11:
Lambda funksiyadan foydalanib berilgan satrli listda qidirilayotgan elemntlarni ajratib oling.
INPUT:
social = ["Instgram", "Facebook", "Telegram", "Tik-Tok", "Radiogram"]
search = 'gram'
OUTPUT: ["Instgram", "Telegram", "Radiogram"]
"""
if 0:
    social = ["Instgram", "Facebook", "Telegram", "Tik-Tok", "Radiogram"]
    search = input("Search: ").lower()
    print(*list(filter(lambda a: a.find(search) != -1, social)))
    # print(*list(filter(lambda x: search in x, social)))
"""
T12:
Lambda funksiyasi orqali listni ichidagi tuplening ma'lumotlarning 2 elementi bo'yicha o'sish tartibida saralang.
Input:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
Output:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
"""
if 0:
    lst = [("English", 88), ("Science", 90), ("Maths", 97), ("Social sciences", 82)]
    sorted_list = sorted(lst, key=lambda a: a[1])
    print(sorted_list)
"""
T13:
Tasavvur qiling-a, sizda berilgan naqshga muvofiq turli xil ranglar
bilan to‘ldirishingiz kerak bo‘lgan kvadratchalar qatori bor.
Kvadratchalarni ketma-ket bo‘yash kerak, ya’ni keyingi kvadrat boshqa
rangda bo‘lsa, qalamni o‘zgartirishingiz kerak bo‘ladi.
Eslatma: Barcha ma’lumotlarni foydalanuvchi kiritishi lozim va
algoritmsiz ishlangan misolga past ball qo‘yiladi.
Ranglar ro‘yxatini oladigan va butun naqshni to‘ldirish uchun zarur
bo‘lgan vaqtning qiymatini (soniyalarda) qaytaradigan funksiyani
yozing.
Bunda:
    • qalamni almashtirish uchun 1 soniya kerak bo‘ladi
    • kvadratni to‘ldirish uchun 2 soniya kerak bo‘ladi

Input: naqsh(["Red", "Blue", "Red", "Blue", "Red"])
Output: 14

Input: naqsh(["Blue"])
Output: 2

Input: naqsh(["Red", "Yellow", "Green", "Blue"])
Output: 11

Input: naqsh(["Blue", "Blue", "Blue", "Red", "Red", "Red"])
Output: 13
"""
if 1:

    def naqsh(str_list: list) -> int():
        new_list = [str_list[0]]
        som = 2
        for i in range(1, len(str_list)):
            if str_list[i] == new_list[-1]:
                som += 2
                new_list.append(str_list[i])
            elif str_list[i] != new_list[-1]:
                som += 3
                new_list.append(str_list[i])
        return som

    enter_list = input("Ranglarni kiriting: ").split()
    print(naqsh(enter_list))
    # print(naqsh(["Red", "Blue", "Red", "Blue", "Red"]))
    # print(naqsh(["Blue"]))
    # print(naqsh(["Red", "Yellow", "Green", "Blue"]))
    # print(naqsh(["Blue", "Blue", "Blue", "Red", "Red", "Red"]))
