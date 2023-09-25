# R7:

# Uchta list ni quyidagicha birlashtiruvchi function tuzing:

# Input:
# ['S001', 'S002', 'S003', 'S004']
# ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# [85, 98, 89, 92]

# Output:
# [
#      {'S001': {'Adina Park': 85}},
#      {'S002': {'Leyton Marsh': 98}},
#      {'S003': {'Duncan Boyle': 89}},
#      {'S004': {'Saim Richards': 92}}
# ]

# Note: natijada list ichida dictionary lar xosil bo'lgan
thisdict = dict()
thislist = list()


def format_list(nums: list, names: list, ages: list) -> list():
    for i in range(len(nums)):
        thisdict[nums[i]] = {names[i]: ages[i]}
    for i in thisdict.items():
        thislist.append({i[0]: i[1]})


nums = ['S001', 'S002', 'S003', 'S004']
names = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
ages = [85, 98, 89, 92]

format_list(nums, names, ages)
print(thislist)
