def elevator(nums: str) -> str:
    # nums = ",".join(nums.split('\n')).split(',')
    print(nums)
    # myDict = dict()
    # for i in range(10, -1, -1):
        # myDict[i] = []
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
lst = list()
for i in range(10):
    lst += list(input())
new = list()
for i in range(len(lst)):
    if lst[i] != ',':
        new.append(lst[i])
        
# 
print(new)

print(elevator(new))