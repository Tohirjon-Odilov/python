isDuble = True
thisset = set()
count = 0
n = None
while isDuble:
    n = int(input("Son kiriting: "))
    thisset.add(n)
    count += 1
    if len(thisset) != count:
        isDuble = False
thisset.remove(n)
thisset.add(n*2)
print(thisset)
