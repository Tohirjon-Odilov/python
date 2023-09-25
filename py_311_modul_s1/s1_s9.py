from my_func import *

# s1
if 0:
    lst = [123, 456, 789, 852, 12, 42, 61, 369]
    print(even(lst))

# s2
if 0:
    lst = [1, 3, 4, 9, 3, 4, 0, -1, 7, 8]
    print(count_ascending_sets(lst))

# s3
if 0:
    son = int(input("Istalgan sonni kiriting (1 dan 1000 gacha): "))
    if son < 1 or son > 1000:
        print("Noto'g'ri kirish! Faqat 1 dan 1000 gacha bo'lgan son kiriting.")
    else:
        natija = pars(son)
    print("Natija:", natija)

# s4
if 0:
    lst = ["Tarvuz", "Nok", "Olma"]
    print(num_sort(lst))

# s5
if 0:
    txt = "Salom Yoz. Olam juda ham go’zal. Imtihon bo’lyapti."
    string = split_txt(txt)
    print("words:", string[0])
    print("sentence:", string[1])

# s6
if 0:
    print(yigindi_yoyish(int(
        input("Istalgan xonali sonni kiriting: "))))

# s7
if 0:
    input_list = [1, 2, 3]
    print(kombinatsiyalarni_topish(input_list))
