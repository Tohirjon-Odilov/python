# def combination(num_list: list, num: int) -> list(tuple()):
    
#     num_list = list(map(str, num_list))
#     lst = list()
#     # for i in num_list:
#         # for j in num_list:
#             # if i != j and not j+i in lst:
#                 # lst.append(i+j)     
#     count = 0
#     while True:
#         # if num_list[:num]:
#         print(num_list[:num])
    
#     return lst

# print(combination([1,2,3,4], 2))

def combinations(lst, length):
    if length == 0:
        return [[]]
    if not lst:
        return []
    without_first = combinations(lst[1:], length)
    with_first = combinations(lst[1:], length-1)
    for item in with_first:
        item.append(lst[0])

    return with_first + without_first

print(combinations([1, 2, 3, 4], 3))  # Natija: [[1, 2], [1, 3], [2, 3]]
