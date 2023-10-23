def chess(nums: list) -> bool:
    return nums[:len(nums)//2] == nums[len(nums)//2:][::-1]

print(chess("1724324856617385"))
print(chess("1827364554637281"))