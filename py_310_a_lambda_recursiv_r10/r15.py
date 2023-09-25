# R 15:

# User o'zi istagancha raqam kiritadi, sizning vazifangiz ularni 10dan
# kattalarini yig'ib return qiladigan function yozing.

# def nums() -> list():
#     lst = list()
#     for i in range(5):
#         n = int(input("Son kiriting: "))
#         if n > 10:
#             lst.append(n)
#     return lst


# print(nums())


# user o'zi istagancha kiritadi
def nums() -> list():
    lst, isEnter = list(), True
    while isEnter:
        n = input("Son kiriting: ")
        if n == '.':
            isEnter = False
            return lst
        n = int(n)
        if n > 10:
            lst.append(n)
    return lst


print(nums())
