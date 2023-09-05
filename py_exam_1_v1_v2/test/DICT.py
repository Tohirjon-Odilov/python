# bo'sh DICT elon qilish -> dct = {} or dct = dict()
# dct = {'Olma':'Apple'} <- = -> dct = dict(Olma: 'Apple')
# DICT bir xil key saqlamaydi, 2ta bo'lsa oxirgini saqlab qoladi

# thisdict = {
#     'Apple' : 'Olma',
#     'Book' : 'Kitob',
#     "Room" : 'Xona'
# }

# print(thisdict) -> {'Apple':'Olma', 'Book':'Kitob','Room':''Xona}
# print(thisdict[0]) -> KeyError
# print(thisdict['Apple']) -> Olma
# print(thisdict["Pen"]) -> KeyError
# print(thisdict.get('Book')) -> Kitob
# print(thisdict.get('Pen')) -> None
# thisdict['Pen'] = 'Ruchka' -> bor bo'lsa qiymatini o'zgartiradi yo'q bolsa qo'shadi
# print(len(thisdict)) -> 3
# print(type(thisdict)) -> dict()
# print(thisdict.keys()) -> ['Apple','Book','Room']
# print(thisdict.values()) -> ['Olma','Kitob','Xona'] 
# thisdict.update({'Apple':'Qizil olma'}) -> 'Apple': 'Qizil olma'
# thisdict.pop('Apple') -> key va value ni olib tashlaydi(return qaytaradi keyini)
# thisdict.popitem() -> oxirgisini olib tashlaydi(return qaytaradi key va valueni)
# del thisdict["Apple"] -> o'chiradi key va valueni(xotiradan ham o'chiradi)
# del thisdict -> xotiradan 'thisdict' ni o'chiradi(keyin topib bo'lmaydi)

# for i in thisdict:
    # print(i) -> faqat keylari chiqadi

# for i in thisdict.keys():
    # print(i) -> faqat keylari chiqadi

# for i in thisdict.values():
    # print(i) -> faqat valuelari chiqadi

# for i in thisdict.items():
    # print(i) -> key va value birga taple() ko'rinishida chiqadi 

# mydict = thisdict -> pointer tenglanib qoldi
# mydict = thisdict.copy() -> faqat key valuealari o'tib qoladi
# mydict = dict(thisdict) -> yangi DICT yasaydi


# stuedents = ['Ali',"Vali",'Sarvar']
# ball = 0
# newDict = dict.fromkeys(stuedents,ball)
# print(newDict) -> {'Ali': 0, "Vali": 0, "Sarvar": 0}