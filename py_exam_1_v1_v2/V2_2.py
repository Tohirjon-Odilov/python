# Problem 1.
if 1:
    mydict = {1: "salom", 2: 123, 3: "hayr", 4: 456, 5: "alvido"}
    new_dict = {i[0]: i[1] for i in mydict.items() if isinstance(i[1], str)}
    key = dict(sorted(new_dict.items(), key=lambda x: x[1]))
    print(key)
if 0:
    mydict = {1: "salom", 2: 123, 3: "hayr", 4: 456, 5: "alvido"}
    new_dict = {key: value for key, value in mydict.items() if isinstance(value, str)}
    sorted_dict = dict(sorted(new_dict.items(), key=lambda item: item[1]))
    print(sorted_dict)
