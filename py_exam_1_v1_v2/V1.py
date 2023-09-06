# PART I

# Question 1.
# Set haqida to'liqroq ma'lumot bering. Misol keltiring.
"""
1. Set o'zida unikal ma'lumotlarni saqlaydi.
2. Indexlanmagan shu sababli index'ga murojaat qilsak xatolik beradi.
3. Xotirada tartibsiz joylashadi.
4. myset = {"salom", "nima" "gaplar"}
"""
# myset = {"salom", "nima", "gaplar"}
# print(myset)

# Question 2.
# Quyidagi kodni izohlang.
# x = 42
# print("no") if x > 42 else print("yes") if x == 42 else print("maybe")
# "yes" chiqadi. If'ning bir qatordagi varianti bo'lib, birinchi shartga to'g'ri kelmaydi.
# shundan so'ng else ichidagi if sharti ishga tushib "yes" print qiladi.


# Question 3.
# Lambda function'ga misol bo'luvchi bir kod yozib bering.
# def myfunc(b):
#     return lambda a: a**b
#
#
# myfunc2 = myfunc(2)
# print(myfunc2(5))


# Question 4.
# Quyidagi kod natijasini izohlang.
# def reverser(a)
# if len(a) > 10 and a[0] = 'a';
# return a[::-1]
# elif len(a) < 10 and a[0] == 'b':
# return a
# print(reverser(input()))

# Ushbu kodda funksiyaning : tushib qolgan syntax error va indentation error beradi.


# Part II

# Problem 1.
# String tipida foydalanuvchi bir satr kiritadi. Maqsadingiz shu satr ichida so'zlar bosh va oxirgi harflarining o'rnini
# almashtirib, paydo bo'lgan satrni chop etuvchi funksiya tuzish.

# text = "London is the capital of great Britain"
# text = text[::-1].split()
# text.reverse()
# text = " ".join(text)

# update
# text = " ".join((map(lambda a: a[::-1], text.split())))
# print(text)

"""
Problem 2.

Foydalanuvchi kiritgan sonning nomini chop etuvchi dastur tuzing. 
Agar foydalanuvchi harf kiritsa, shu harfning o'zbek
alifbosidagi o'rnini chop eting.
"""

if 1:

    def alpha_number(num):
        alpha = {
            0: "nol",
            1: "bir",
            2: "ikki",
            3: "uch",
            4: "toʻrt",
            5: "besh",
            6: "olti",
            7: "yetti",
            8: "sakkiz",
            9: "to'qqiz",
            10: "oʻn",
            20: "yigirma",
            30: "o'ttiz",
            40: "qirq",
            50: "ellik",
            60: "oltmish",
            70: "yetmish",
            80: "sakson",
            90: "to'qson",
            100: "bir yuz",
            100: "ikki yuz",
            100: "uch yuz",
            100: "to'rt yuz",
        }

        if num in alpha:
            return alpha[num]
        elif 10 < num < 100 and num % 10 != 0:
            tens = num // 10 * 10
            units = num % 10
            return alpha[tens] + " " + alpha[units]
        else:
            return "Invalid number entered"

    def letter_position(letter):
        letter = letter.lower()
        alpha = "abcdefghijklmnopqrstuvwxyz"
        if letter in alpha:
            index = alpha.index(letter) + 1
            return index
        else:
            return "Invalid letter entered"

    try:
        user_input = input("Enter a letter or a number: ")
        if user_input.isdigit():
            number = int(user_input)
            if 0 <= number <= 100:
                name = alpha_number(number)
                print(name)
            else:
                print("Please enter a number between 0 and 100.")
        else:
            letter_index = letter_position(user_input)
            print(letter_index)
    except Exception as e:
        print("Please enter a valid number or letter.", e)


# Problem 3.
# Biror dictionary tipidagi ma'lumotni fayl ichiga dictionary ko'rinishida yozuvchi,
# va shundan so'ng xuddi shu fayl ichidan
# o'qib yana dictionary ko'rinishiga keltirib beruvchi dastur tuzing. Misollar quyida keltirilgan.
if 0:
    mydict = {
        "first_name": "John",
        "last_name": "Doe",
        "age": 34,
        "student": False,
        "worker": True,
    }

    with open("file.txt", "w") as f:
        f.write("{")
        for key, val in mydict.items():
            if type(val) == str:
                f.write(f'"{key}": "{val}",')
            else:
                f.write(f"{key}: {val},")

        f.write("}")
if 0:
    # update
    mydict = {
        "first_name": "John",
        "last_name": "Doe",
        "age": 34,
        "student": False,
        "worker": True,
    }

    with open("file.txt", "w") as f:
        f.write("{\n")
        for key, val in mydict.items():
            if isinstance(val, str):
                f.write(f'    "{key}": "{val}",\n')
            else:
                f.write(f'    "{key}": {val},\n')
        f.write("}\n")

if 0:
    import json

    data = {
        "first_name": "John",
        "last_name": "Doe",
        "age": 34,
        "student": False,
        "worker": True,
    }

    with open("data.json", "w") as file:
        json.dump(data, file)

# Problem 4.

# Foydalanuvchi matematik ifodani input orqali kiritadi va sizning vazifangiz ushbu matematik ifodada nechta matematik
# amallar takrorlanganligi haqida ma’lumotni chiqarib berish.
# (Matematik amallar: +, -, *, /, %, () )

if 0:
    math = "2+3*5-2+9/(2+7/5-123)"

    print(
        f"+ amali {math.count('+')}ta, "
        f"- amali {math.count('-')}ta, "
        f"* amali {math.count('*')}ta, "
        f"/ amali {math.count('/')}ta, "
        f"() amali {math.count('(')}ta",
        end=" ",
    )

# update
# math = "2+3*5-2+9/(2+7/5-123)(3*20)"
#
# operators = "+-*/()"
#
# operator_counts = {operator: math.count(operator) for operator in operators}
# print(operator_counts)
#
# operator_string = ", ".join(
#     [f"{operator} amali {count}ta" for operator, count in operator_counts.items()]
# )
#
# print(operator_string)
