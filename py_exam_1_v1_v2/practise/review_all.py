# Problem 1.
if 0:
    txt = "London is the capital of great Britain".split()
    txt = list(map(lambda word: word[::-1], txt))
    print(" ".join(txt))

if 1:

    def number(num: int):
        number_name = {
            1: "bir",
            2: "ikki",
            3: "uch",
            4: "to'rt",
            5: "besh",
            6: "olti",
            7: "yetti",
            8: "sakkiz",
            9: "to'qqiz",
            10: "o'n",
            20: "yigirma",
            30: "o'ttiz",
            40: "qirq",
            50: "ellik",
            60: "oltmish",
            70: "yetmish",
            80: "sakson",
            90: "to'qson",
            100: "yuz",
            200: "ikki yuz",
            300: "uch yuz",
            400: "to'rt yuz",
            500: "besh yuz",
            600: "olti yuz",
            700: "yetti yuz",
            800: "sakkiz yuz",
            900: "to'qqiz yuz",
        }
        if num in number_name:
            return number_name[num]
        elif 10 < num < 100 and num % 10 != 0:
            tens = num // 10 * 10
            units = num % 10
            return number_name[tens] + number_name[units]
        else:
            raise ValueError("Invalid number")


def alpha(alp: str):
    alp = alp.lower()
    alphabit = "abcdefghijklmnopqrstuvwxyz"

    for i in alphabit:
        if i == alp:
            return alphabit.index(i) + 1
        else:
            continue
