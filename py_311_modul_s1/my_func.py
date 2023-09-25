from itertools import permutations


# s1
def even(lst: list) -> list:
    return list(filter(lambda a: not (int(str(a)[0]) % 2), lst))

# s2


def count_ascending_sets(lst):
    count = 0
    current_set = []

    for num in lst:
        if not current_set or (num >= current_set[-1]):
            current_set.append(num)
        else:
            if len(current_set) > 1:
                count += 1
            current_set = [num]

    if len(current_set) > 1:
        count += 1

    return count


# s3
birliklar = ["", "bir", "ikki", "uch", "to'rt", "besh", "olti", "yetti",
             "sakkiz", "to'qqiz"]
onliklar = ["", "o'n", "yigirma", "o'ttiz", "qirq", "ellik", "oltmish",
            "yetmish", "sakson", "to'qson"]
yuzlar = ["", "bir yuz", "ikki yuz", "uch yuz", "to'rt yuz", "besh yuz",
          "olti yuz", "yetti yuz", "sakkiz yuz", "to'qqiz yuz"]


def pars(son):
    yuz_miqdori = son // 100
    onlik_miqdori = (son % 100) // 10
    birlik_miqdori = son % 10

    natija = ""
    if yuz_miqdori > 0:
        natija += yuzlar[yuz_miqdori] + " "
    if onlik_miqdori > 0:
        natija += onliklar[onlik_miqdori] + " "
    if birlik_miqdori > 0:
        natija += birliklar[birlik_miqdori]

    return natija


# s4
def num_sort(lst: list) -> list:
    return sorted(lst, key=len)


# s5
def split_txt(txt: str) -> str:
    words = list(map(lambda a: a.replace(".", ''), txt.split()))
    sentence = list(filter(lambda a: len(a) != 0, txt.split(".")))
    return [words, sentence]


# s6
def yigindi_yoyish(son):
    str_son = str(son)
    return "+".join([d + "0" * (len(str_son) - i - 1)
                     for i, d in enumerate(str_son)])


# s7
def kombinatsiyalarni_topish(input_list):
    result = list(map(lambda a: list(a),
                      list(permutations(input_list))))
    return result
