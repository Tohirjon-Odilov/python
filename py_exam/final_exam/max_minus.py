def the_max_minus(nums: list):
    max_minus, idx = nums[0]-nums[1], [0, 1]
    for i in range(2, len(nums)-1):
        if max_minus < nums[i+1]-nums[i]:
            max_minus, idx = nums[i+1]-nums[i], [i, i+1]
    return max_minus, idx

nums = list(map(int, input("N = ").split()))
minus, ind = the_max_minus(nums)
print(f"{minus}({nums[ind[0]]} va {nums[ind[1]]})")