def minimal_change(num: int) -> int:
    num = str(num)
    new_num = list(map(lambda a: a*len(num), list(num)))
    res = list()
    for i in num:
        nums = list()
        i = int(i)
        for j in num:
            if i != j:
                j = int(j)
                nums.append(abs(i-j))
        res.append(sum(nums))

    id = min(res)
    return f"{new_num[res.index(id)]} -> {id}"

print(minimal_change(293))
print(minimal_change(8471))