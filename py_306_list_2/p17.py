# P17:

# 1 dan n gacha bo'lgan oraliqda berilgan ro'yxatni birlashtirish orqali
# ro'yxat yaratish uchun Python dasturini yozing. Tahrirlovchiga   o'ting.
# Namuna ro'yxati : ['p', 'q']
# n =5
# Namuna Chiqish: ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4' , 'q4', 'p5', 'q5']

lst1 = ['p', 'q']
n = int(input("Son kiriting: "))
lst2 = list()
count = 0
for i in range(n):
    lst2.append(lst1)
lst1 = list()
for i in range(len(lst2)):
    lst1.append(lst2[i][0] + str(i+1))
    lst1.append(lst2[i][1] + str(i+1))
print(lst1)
