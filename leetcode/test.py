
        

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

# 350. Intersection of Two Arrays II
if 0:
    class Solution:
        def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
            # x = list(set(nums1) & set(nums2))
            # a = str(nums1).count("".join(x))
            # b = str(nums2).count("".join(x))
            # x = str(x) * int(a if a > b else b)
            num3 = list()
            for el in nums1:
                if el in nums2:
                    num3.append(el)
            return num3
    
    print(Solution().intersect([1,2,2,1], [2,2]))

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
        


