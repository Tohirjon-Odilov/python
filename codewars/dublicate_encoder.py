# def duplicate_encode(word):
#     word = word.lower()
#     return "".join(map(lambda el: "(" if word.count(el) == 1 else ")", word))


def duplicate_encode(word):
    word = word.lower()
    return "".join("(" if word.count(el) == 1 else ")" for el in word)


print(duplicate_encode("SucCess"))
