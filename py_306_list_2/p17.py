# P17:

# 1 dan n gacha bo'lgan oraliqda berilgan ro'yxatni birlashtirish orqali
# ro'yxat yaratish uchun Python dasturini yozing. Tahrirlovchiga   o'ting.
# Namuna ro'yxati : ['p', 'q']
# n =5
# Namuna Chiqish: ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4' , 'q4', 'p5', 'q5']

lst1 = ['p', 'q']
n = int(input("Son kiriting: "))
# n = 5
lst2 = list()

for i in range(n+1):
    lst2.append(lst1)
lst1 = list()

for i in range(1, len(lst2)):
    lst1.append(lst2[i][0] + str(i))
    lst1.append(lst2[i][1] + str(i))
print(lst1)

# lst = list()

# n = int(input('son kiriting: '))

# for i in range(1,n+1):
#     lst.insert(n*2,('p'+str(i)))
#     lst.insert(n*2,('q'+str(i)))

# print(lst)
