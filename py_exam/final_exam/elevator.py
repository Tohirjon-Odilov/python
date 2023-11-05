def elevator(nums: str) -> str:
    print("\n")
    nums = ",".join(nums.split('\n')).split(',')

    myDict = {i: [] for i in range(10, -1, -1)}

    for i in nums:
        if i.isdigit():
            i = int(i)
            myDict[i].append(i)
            
    for key, value in myDict.items():
        if not value:
            myDict[key].append("-")

    result = str()
    for i in myDict.values():
        result += ",".join(list(map(str, i))) + "\n"
    return result[:-1]

lst = str()
for i in range(10):
    lst += input()+'\n'

print(elevator(lst))