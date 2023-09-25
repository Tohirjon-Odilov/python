# R6:

# Function tuzing. Bu function, listning ichidagi tuple ni listga o'girib
# bersin.

# Input:     [(1, 2), (2, 3), (3, 4)]
# Output:  [[1, 2], [2, 3], [3, 4]]

# —————————————————————————

# Input:     [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
# Output:  [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]

def tuple_to_list(lst: list()):
    return list(map(list, lst))


# lst = [(1, 2), (2, 3), (3, 4)]
lst = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
lst = tuple_to_list(lst)
print(lst)
