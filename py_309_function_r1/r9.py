# R9:

# Ichma ich list qabul qiluvchi va quyidagicha dictionary qaytaruvchi
# function tuzing

# Input:
# [
#       [1, 'Jean Castro', 'V'],
#       [2, 'Lula Powell', 'V'],
#       [3, 'Brian Howell', 'VI'],
#       [4, 'Lynne Foster', 'VI'],
#       [5, 'Zachary Simon', 'VII']
# ]

# Output:
# {
#      1: ['Jean Castro', 'V'],
#      2: ['Lula Powell', 'V'],
#      3: ['Brian Howell', 'VI'],
#      4: ['Lynne Foster', 'VI'],
#      5: ['Zachary Simon', 'VII']
# }

def format_to_dict(lst: list) -> list():
    thisdict = dict()
    i = 0
    while i in range(len(lst)):
        del lst[i][0]
        i += 1
    for i, el in enumerate(lst):
        thisdict[i+1] = el
    return thisdict


lst = [[1, 'Jean Castro', 'V'],
       [2, 'Lula Powell', 'V'],
       [3, 'Brian Howell', 'VI'],
       [4, 'Lynne Foster', 'VI'],
       [5, 'Zachary Simon', 'VII']
       ]


print(format_to_dict(lst))
