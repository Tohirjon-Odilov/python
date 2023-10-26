def minimal_change(num: int) -> int:
    num = str(num)
    new_num = list(map(lambda a: a*len(num), list(num)))
    lst = list()
    for i in num:
        nums = list()
        i = int(i)
        for j in num:
            if i != j:
                j = int(j)
                nums.append(abs(i-j))
        lst.append(sum(nums))

    id = min(lst)
    res = [f"{new_num[i]} -> {id}" for i in range(len(lst)) if id == lst[i]]
    return "\n".join(res)

print(minimal_change(int(input(">>> "))))

# print(minimal_change(293))
# print(minimal_change(8471))