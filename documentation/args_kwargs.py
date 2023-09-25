# args------------------------

# def noname(*args):
#     print(*args) # 10 20 30 
# noname(10,20,30)

# # ---------------------------

# def noname(name, *args):
#     print(name) # 10
#     print(*args) # 20 30
# noname(10,20,30)

# # kwargs---------------------

# def noname(**kwargs):
#     print(kwargs) #{'name': 'John', 'age': 23}
#     print(*kwargs) # name age
# noname(name = 'John', age = 23)

# # --------------------------

# def noname(count, *args, **kwargs):
#     print(count) # 10
#     print(args) # ('Najot Talim', 'Haad')
#     print(kwargs) # {'name': 'John', 'age': 23, 'adress': 'Toshkent'}
# noname(10, "Najot Talim", "Haad", name = "John", age = 23, adress = 'Toshkent')

# by default ---------------

# malum bir qiymatlari berilmasa ham ishlaydi

# def noname(count='', *args, **kwargs):
#     print(count) # 10
#     if args:
#         print(args) # ('Najot Talim', 'Haad')
#     if kwargs:
#         print(kwargs) # {'name': 'John', 'age': 23, 'adress': 'Toshkent'}
# noname(10, "Najot Talim", "Haad", name = "John", age = 23, adress = 'Toshkent')

# -----------------------

# funksiyaga funksiya bersih

# def noname(count='', key = None):
#     x = key
#     return x(count)
# print(noname(10, lambda i : str(i))) # 10
# print(type(noname(10, lambda i : str(i)))) # <class 'str'>