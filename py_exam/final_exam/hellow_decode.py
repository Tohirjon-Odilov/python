def decode(word: str, letters: dict) -> str:
    reply = ""
    used = letters.copy()
    for i in word:
        c = word.count(i)
        for l, n in letters.items():
            if c == n and used[l] != 0:
                used[l]=used[l]-1
                reply += l
                break

    return reply

# word = input("Input Decode word: ")
# n = int(input("N="))
# data = {}
# for i in range(n):
#     l = input("Input: ").split(":")
#     data[l[0]] = int(l[1])
# print(decode(word, data))

print(decode("?*!*!*", {'b': 1, 'a': 3, 'n': 2}))
print(decode("!@**?", {'H': 1,'E': 1,'L': 2, 'O': 1}))