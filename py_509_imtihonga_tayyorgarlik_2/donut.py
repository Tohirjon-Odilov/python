def dublicate_zeros(nums:str) -> list[int]:
    nums = eval(nums)
    num = list()
    for el in nums:
        if el == 0:
            num.append(0)
        num.append(el)
    
    return num

print(dublicate_zeros("[1,0,2,3,0,4,5,0]"))
print(dublicate_zeros("[0,0,0,0]"))
print(dublicate_zeros("[100, 10, 0, 0, 101, 1000]"))
