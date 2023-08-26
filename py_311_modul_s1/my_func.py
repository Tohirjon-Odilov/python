def even(lst):
    return list(filter(lambda a: not (int(str(a)[0]) % 2), lst))
