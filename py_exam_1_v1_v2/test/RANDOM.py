# import random

# random.random() -> 0 va 1 oralig'ida float qiymat qaytaradi
# random.uniform(1,10) -> 1 dan 10 gacha float qiymat qaytaradi
# random.randint(1,10) -> 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 lardan birini qaytaradi
# random.randrange(1,10) -> 1, 2, 3, 4, 5, 6, 7, 8, 9 lardan birini qaytaradi
# random.randrange(1,10,2) -> 1 3 5 7 9 11 lardan birini qaytaradi

# country = ['us','uz','en','gr','fr','ru']
# random.choice(country) -> ichidan birortasini randomli olib qaytaradi
# random.sample(country, k=2) -> ichidan 2 tasini randomli olib listga solib qaytaradi
# random.choices(country, k = 20) -> ichidan 20 ta randomli olib(takrorlanishi mumkin) qaytaradi
# random.choices(country, k = 10, weights=[3,4,5,4,4,4]) -> malum bir elementlarda ko'roq chiqaradigan qilish mumkin
# random.shuffle(country) -> country dagi barcha elementlarni aralashtirib tashlaydi(return qaytarmaydi)

# txt = ['s','a','l','o','m']
# random.shuffle(txt)
# print(''.join(txt)) -> bir so'zni har doin har xil qilib chiqaradi(salom,nalos,asmol,...)