def caesar_cipher(text, key):
    # text = text.lower()
    # shifr = list("abcdefghijklmnopqrstuvwxyz")
    # res = list()
    # 
    # for i in range(len(shifr)):
        # for j in text:
            # if shifr[i] == j:
                # res.append(shifr[i+key])

    return "".join(list(chr(ord(i)+key) for i in text))
    # return "".join(res)

print(caesar_cipher("hello", 5))
print(caesar_cipher("hello world", 1))
print(caesar_cipher("z", 2))