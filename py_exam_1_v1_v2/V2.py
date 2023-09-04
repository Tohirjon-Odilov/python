"""
Part I.


Question 1.

Dictionary
haqida to’liq ma’lumot bering. Misol keltiring.
"""
"""
Dictionry bu ma'lumot strukturasi bo'lib juda keng qo'llaniladi hamda, 
{} yordamida ochiladi.
O'zida key value sifatida ma'lumotlarni saqlay oladi. Key va value o'rtasida = emas
: dan foydalanamiz. Key'lar har doim immutable va unikal bo'lishi kerak. Agar bir xil key
uchrab qolsa oxirgi key'ni olib ketadi. Ichma ich dictionary yoza olamiz.
Dictionary o'zida har qanday ma'lumot'ni saqlay oladi.
"""
if 0:
    mydict = {
        "name": "Tohirjon",
        "age": 21,
        "country": "Uzbekistan",
    }

"""
Question 2.

Quyidagi kod natijasini izohlang:
"""
if 0:
    print([i for i in range(10) if i % 2 == 0])
"""
range(10) funksiyasi 0 9 gacha sonlarni o'z ichaga oladi.
Va shu sonlar ichidan faqat juftlarini ya'ni shartga to'g'ri kelganlarini 
kvadratga oshirib print() funksiyasi yordamida
terminalga list ko'rinishida chiqarib beradi.
"""

"""
Question 3.

Istisnoli(try except) holat nima? Javobingizni kod misolida izohlang.
"""
if 0:
    try:  # bu kodlarni sinab ko'rish bloki
        n = int(input())
    except ValueError:  # agar xatolik ValueError bilan tugasa bu blok ishlaydi
        print("Kiritilgan ma'lumotni son'ga o'girish mobaynida xatlik yuzaga keldi.")
    else:  # agar kod muvaffaqqiyatli yakin topsa unda bu blok ishlaydi
        print("Done")
    finally:  # ushbu blok har doiom ishga tushadi
        print("Finish")
"""
Question 4.

Quyidagi kod natijasini izohlang:

def print_conditions(a, b, c):
    if a == "Kate":
        print(a, b, c)
    elif b = "John":
        print(b, a, c)
    elif c = "Jonathan"
        print(c, b, a)
print_conditions(b:input(), c:input(), a:input())

Kod ishga tushganda xatolik yuz beradi.
Ya'ni funkisyaning argumentlariga qiymat o'zlashtirayotganimizda ikki nuqta bilan emas
barobar bilan ishlashimiz kerak bo'ladi. Funksiya ichidagi 2 va 3 shartlarda
solishtirish operatori o'rniga o'zlashtirish operatori ishlatilgan
Hamda 3 shartda, shartdan so'ng ikki nuqta qolib ketgan
"""
#######################################################################################
"""
Part II


Problem 1.

List ichi foydalanuvchi tomonidan bir necha so'z bilan to'ldiriladi. Maqsadingiz shu so'zlar orasidan k yoki K harflari
qatnashgan so'zlarni chop etuvchi funksiya yozish.
"""

if 0:
    print("Enter 5 words:")
    txt = list()
    for _ in range(5):
        txt.append(input())
    print(*list(i for i in txt if i.lower().find("k") != -1))

# update
if 0:
    print("Enter 5 words:")
    txt = list(input() for _ in range(5))
    words_with_k = [word for word in txt if "k" in word.lower()]
    print()
    print(*words_with_k)

"""
Problem 2.

Foydalanuvchi str tipida istalgan uzunlikdagi satr kiritadi. 
Maqsadingiz shu satr ichidan unli harf bilan boshlangan so'zlarni
ekranga chop etuvchi dastur tuzish.
"""
if 0:
    txt = input("Enter sentences:\n>>> ").split()
    # vovel = ["a", "e", "u", "i", "o"]
    vovel = set("aeuio")
    first_vovel = list(word for word in txt if word[0].lower() in vovel)
    print(*first_vovel)

"""
Problem 3.

To'rtta amal(+, -, *, /)ni bajaruvchi kalkulyator tuzing. 
Dasturda yuzaga kelishi mumkin bo'lgan hamma istisnoli (try except)
holatlarni hisobga oling ( ValueError , ZeroDivisionError ). 
Dastur funksiyalarni ishlatgan holda yozilishi shart.
"""
if 0:
    arifmetic_operations = "+ - * /".split()

    def calculate(a: int, b: int, arifmetic: str) -> int:
        if arifmetic == "+":
            return a + b
        elif arifmetic == "-":
            return a - b
        elif arifmetic == "*":
            return a * b
        elif arifmetic == "/":
            return a // b

    try:
        user_input_a = int(input("A son kiriting:\n>>> "))
        user_input_b = int(input("B son kiriting:\n>>> "))
        user_input_arifmetic = input(
            "Amal ni kiriting. << \033[1;31m+\033[1;0m >> << \033[1;31m-\033[1;0m >> "
            "<< \033[1;31m*\033[1;0m >> << \033[1;31m/\033[1;0m >>\n>>> "
        )
        if user_input_arifmetic in arifmetic_operations:
            ssum = calculate(user_input_a, user_input_b, user_input_arifmetic)
            print(f"\n{user_input_a}{user_input_arifmetic}{user_input_b}={ssum}")
    except ValueError:
        print("\n\033[1;31mIltimos faqat son kiriting!")
    except ZeroDivisionError:
        print("\n\033[1;31mNol'ga (0) bo'lish mumkin emas!!!")
if 0:
    arithmetic_operations = "+ - * /".split()

    def calculate(a: int, b: int, arithmetic: str) -> int:
        """
        Kalkulyator
        """
        if arithmetic == "+":
            return a + b
        elif arithmetic == "-":
            return a - b
        elif arithmetic == "*":
            return a * b
        elif arithmetic == "/":
            if b == 0:
                raise ValueError("Nol'ga bo'lish mumkin emas")
            return a // b
        else:
            raise ValueError("Noto'g'ri amal kiritdingiz")

    try:
        user_input_a = int(input("A son kiriting:\n>>> "))
        user_input_b = int(input("B son kiriting:\n>>> "))
        user_input_arithmetic = input(
            "Amalni kiriting. << \033[1;31m+\033[1;0m >> << \033[1;31m-\033[1;0m >> "
            "<< \033[1;31m*\033[1;0m >> << \033[1;31m/\033[1;0m >>\n>>> "
        )
        if user_input_arithmetic in arithmetic_operations:
            result = calculate(user_input_a, user_input_b, user_input_arithmetic)
            print(f"\n{user_input_a} {user_input_arithmetic} {user_input_b} = {result}")
        else:
            raise ValueError("Noto'g'ri amal kiritdingiz")
    except ValueError as e:
        print(f"\n\033[1;31mXatolik: {e}")
    except ZeroDivisionError:
        print("\n\033[1;31mNol'ga (0) bo'lish mumkin emas!!!")
    except Exception as e:
        print(f"\n\033[1;31mXatolik: {e}")


"""
Problem 4.
Fayl ichida bir necha qatorda matn berilgan bo'ladi. 
Maqsadingiz shu fayl ichidagi so'zlarni alifbo tartibida saralash.
"""
if 0:
    with open("V2_problem_4_file.txt", "r+") as f:
        txt = f.read().split()
        f.seek(0)
        txt = sorted(txt, key=lambda a: a.lower())
        for i in txt:
            f.write(i + " ")
# update
if 0:
    with open("V2_problem_4_file.txt", "r") as f:
        txt = f.read().split()
        txt = sorted(txt, key=lambda a: a.lower())

    with open("V2_problem_4_file.txt", "w") as f:
        f.write(" ".join(txt))
if 0:
    # chatgpt version
    # Faylni o'qish
    with open("V2_problem_4_file.txt", "r") as file:
        lines = file.readlines()

    # So'zlarni olish va alifbo tartibida saralash
    words = []
    for line in lines:
        words.extend(line.split())

    sorted_words = sorted(words, key=lambda x: x.lower())

    # Saralgan so'zlarni ekranga chiqarish
    for word in sorted_words:
        print(word)
