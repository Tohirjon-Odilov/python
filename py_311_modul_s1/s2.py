# S2:
# Sizga list berilgan. Listdagi o'sish tardibida kelgan sonlar to'plamlar
# sonini hisoblab qaytaruvchi funktsiya yozing

# Input:
# [1, 3, 4, 9, 3, 4, 0, -1, 7, 8 ]
# Output:
# Masalan lst = [1, 3, 4, 9, 3, 4, 0, -1, 7, 8 ]
# Bu listda o'sish tardibida kelgan to'plamlar bu
# " 1, 3, 4, 9 "
# " 3, 4 "
# " -1, 7, 8 "
# Ularning soni 3ta

from my_func import count_ascending_sets

lst = [1, 3, 4, 9, 3, 4, 0, -1, 7, 8]

count_ascending_sets(lst)
