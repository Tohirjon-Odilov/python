def saylov(text: str) -> str:
    words = text.split()
    total_words = len(words)
    count = total_words // 2
    names = {i: 0 for i in words}
    max_word = None

    for word in words:
        if word in names:
            if max_word is None:
                max_word = word
            names[word] += 1
    for i in names:
        if names[i] > count:
            return i
        
    max_word = max(names, key = lambda x: names[x])
    second_max_word = max(names, key=lambda x: names[x] if x != max_word else -1)
    return f"{max_word}\n{second_max_word}"

# print(saylov("Sanjar Botir Sanjar"))
print(saylov("Sanjar Farrux Go'zal Farrux Farrux Sanjar Go'zal"))
