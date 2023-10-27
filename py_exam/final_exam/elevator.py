def elevator(nums: str) -> str:
    print("\n")
    nums = ",".join(nums.split('\n')).split(',')

    myDict = {i: [] for i in range(10, -1, -1)}
    # myDict = dict()
    # for i in range(10, -1, -1):
        # myDict[i] = []

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

# print(elevator('''1,4,3,2
# 1,10,2
# -
# 3,6,4,5,6
# -
# -
# 0,0,0
# -
# 4
# 6,5,2
# -'''))

lst = str()
for i in range(10):
    lst += input()+'\n'

print(elevator(lst))