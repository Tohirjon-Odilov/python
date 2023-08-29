# def accum(s):
#     text = str()
#     text2 = list()
#     for i, el in enumerate(s.lower(), 1):
#         text = el * i
#         text2.append(text.capitalize())
#     return "-".join(text2)
#
#


def accum(txt):
    return "-".join((el * i).title() for i, el in enumerate(txt, 1))


print(accum("RqaEzty"))  # -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
