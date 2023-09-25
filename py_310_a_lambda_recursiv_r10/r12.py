# R12:

# Kiritilgan raqamni ikkilik sanoq sistemasiga o'tkazubchi funksiya
# yozing.

# def binary(n: int) -> int():
#     thislist = list()
#     while n != 0:
#         div = n % 2
#         thislist.append(div)
#         n //= 2
#     binar = str()
#     for i in thislist[::-1]:
#         binar += str(i)
#     return int(binar)


# print(binary(int(input("Son kiriting: "))))


# with function
def binar(n: int) -> bin:
    return bin(n)


print(binar(int(input("Son kiriting: ")))[2:])
