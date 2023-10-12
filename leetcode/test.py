# 896. Monotonic Array
if 1:
    class Solution:
        def isMonotonic(self, nums: list[int]) -> bool:
            return True if nums == list(sorted(nums)) or list(reversed(sorted(nums))) == nums else False
        
    print(Solution().isMonotonic([1,2,2,3]))
    print(Solution().isMonotonic([6,5,4,4]))
    print(Solution().isMonotonic([6,3,4,2]))


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
        






