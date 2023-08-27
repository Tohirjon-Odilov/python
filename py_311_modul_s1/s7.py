# S7:

# Foydalanuchi tomonidan list kiritiladi. Shu listni kombinatsiyalarini
# quyidagi ko'rinishda ekranga chiqaruvchi funksiya yarating.
# INPUT = [1, 2 ,3]
# OUTPUT = [[1, 2, 3] , [3, 2, 1] ,[1, 3, 2] ,[3, 1, 2] ,[2, 1, 3] ,[2, 3, 1] ]
from itertools import permutations


def kombinatsiyalarni_topish(input_list):
    result = list(map(lambda a: list(a),
                      list(permutations(input_list))))
    return result


input_list = [1, 2, 3]
output = kombinatsiyalarni_topish(input_list)
print(output)
