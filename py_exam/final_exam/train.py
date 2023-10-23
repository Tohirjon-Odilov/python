def train(N:int, *name: str) -> str:
    name, myDict = list(name), dict()
    names, nums = list(), list()
    for i in name:
        i = i.strip().split()
        names.append("".join(i[:1]))
        nums.append(" ".join(i[1:]))
    for i in range(len(names)):
        myDict[names[i]] = list(map(int, nums[i].split(" ")))
    bekat = dict()
    names = None
    for i in range(1, N+1):
        count = 0
        for j in myDict:
            if i > myDict.get(j)[0] and i <= myDict.get(j)[1]:
                if not names:
                    names = f"{i-1}-{i}"
                count += 1
                bekat[f"{i-1}-{i}"] = count
    nums.clear()
    for i in bekat:
        if bekat.get(names) <= bekat.get(i):
            names = i
    for i in bekat:
        if bekat.get(names) == bekat.get(i):
            nums.append(i)
        
    return nums


n = int(input("N="))
m = int(input("M="))
name = list()
for i in range(m):
    name.append(input())
    
print(*train(n, *name), sep="\n")
# print(*train(5, "Sanjar 3 5", "Baxrom 1 4", "Kamola 1 2"), sep="\n")