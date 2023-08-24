# Q 11:

# User n kiritadi va setga shuncha ma'lumot qo'shib boriladi. Yakunda esa siz
# user nechta dublikat ma'lumot qo'shganini ekranga chiqaring.
isDuble = True
count = 0
thisset = set()
n = int(input("Set'ning len'nini kiriting: "))
while n > 0:
    num = int(input("Son kiriting: "))
    thisset.add(n)
    set_len = len(thisset)
    print(len(thisset), set_len)
    if set_len == len(thisset):
        count += 1
    n -= 1
print(count)
