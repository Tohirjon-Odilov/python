"""
Problem 1.
"""
if 0:
    text = input("Text = ")
    harf = input("harf = ")

    if text.count(harf) == 1:
        print(text.find(harf))
    else:
        idx = None
        for i, el in enumerate(text):
            if el == harf:
                idx = i
        print(idx)
"""
Problem 2
"""
if 1:

    def only_dublicate(deflist: list):
        deflist = list(map(str, deflist))
        deflist = ",".join(deflist).split(",")
        return list(map(int, list(filter(lambda a: deflist.count(a) >= 2, deflist))))

    mylist = [3, 3, 4, 5, 6, 6]
    print(only_dublicate(mylist))
if 0:
    txt = str()
    mylist = int()
    count = int()
    while txt != "c":
        txt = input(">>> ")
        if txt != "c":
            count += 1
            mylist += int(txt)
    print(f"Sum of {count} number: {mylist}")
if 0:
    with open("V1_2_all_words.txt", "r") as fread:
        txt = fread.read().split()
        for i in txt:
            if "k" in i.lower():
                with open("V1_2_words_attend_K.txt", "a") as kword:
                    kword.write(i + "\n")
            if "a" in i.lower():
                with open("V1_2_words_attend_A.txt", "a") as aword:
                    aword.write(i + "\n")
