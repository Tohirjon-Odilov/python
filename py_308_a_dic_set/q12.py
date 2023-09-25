# Q 12:

# User n va max,min sonini kiritadi va setga  n ta ma'lumot qo'shadi.
# Ma'lumot qo'shish jarayonida, user kiritgan son max va min oralig'iga
# tushmasa, setning oxirgi elementini o'chirib tashlasin va kiritilgan
# ma'lumot setga qo'shilsin.

# Setga n ta ma'lumot qo'shilganidan so'ng, ekranga set va boya o'chirib
# tashlangan raqamlar chiqsin.

n = int(input("Set'ni len'nini kiriting: "))
mn = int(input("Min sonini kiriting: "))
mx = int(input("Max sonini kiriting: "))

count = 0
thisset = set()
delset = set()
while n:
    if n == len(thisset):
        break
    nums = int(input("Son kiriting: "))
    if not (mn <= nums and nums <= mx) and len(thisset):
        delset.add(thisset.pop())
    thisset.add(nums)

    print(len(thisset))
print("thisset", thisset)
print("delset", delset)
