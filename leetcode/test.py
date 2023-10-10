# 1480. Running Sum of 1d Array
if 0:
    class Solution:
        def runningSum(self, nums: list[int]) -> list[int]:
            sum = [nums[0]]
            for i in range(1, len(nums)):
                sum.append(sum[-1]+nums[i])
            return sum
            
            
# --------------------    
    print(Solution().runningSum([1,2,3,4])) # [1,3,6,10]



# 941. Valid Mountain Array
if 0:
    class Solution:
        def validMountainArray(self, arr: list[int]) -> bool:
            if len(arr) > 3:
                return False
            if arr[0] >= arr[1]:
                return False
    
    print(Solution().validMountainArray([2,5,5])) #False
    print(Solution().validMountainArray([2,1])) #False
    print(Solution().validMountainArray([0,3,2,1])) #True
        




