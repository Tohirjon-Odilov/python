import re

# def reverse_words(text):
#     text = text.split()
#     rev = []
#     for i in text:
#         rev.append(i[::-1])
#     return " ".join(rev)
#
#
# print(reverse_words("This is an example!"))


def reverse_words(str):
    return " ".join(s[::-1] for s in str.split(" "))


print(reverse_words("slom dunyo nima gaplar"))


def reverse_words(str):
    return re.sub(r"\S+", lambda w: w.group(0)[::-1], str)
