# 1. Two Sum
if 0:
    class Solution(object):
        def twoSum(self, nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
            """
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if nums[i] + nums[j] == target:
                        return [i, j]
    nums = [2,7,11,15]
    target = 9
    pr = Solution().twoSum(nums, target)
    print(pr)

# 9. Palindrome Number
if 0:
    class Solution(object):
        def isPalindrome(self, x):
            """
            :type x: int
            :rtype: bool
            """
            x = str(x)
            for i in range(len(x)//2):
                if x[i] == x[len(x)-i-1]:
                    print(x[i])

    pr = Solution().isPalindrome(121)
    # print(pr)
 
# 349. Intersection of Two Arrays

if 0:
    class Solution:
        def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
            return list(set(nums1).intersection(set(nums2)))
    
    pr = Solution().intersection([1,2,2,1],[2,2])
    print(pr)           

if 0:
    # 1351. Count Negative Numbers in a Sorted Matrix

    class Solution(object):
        def countNegatives(self, grid:list):
            """
            :type grid: List[List[int]]
            :rtype: len(x)-i-1int
            """
            count = 0
            for i in grid:
                for j in i:
                    if j < 0:
                        count += 1
            return count
        
    # update version
    class Solution1(object):
        def countNegatives(self, grid):
            """
            :type grid: List[List[int]]
            :rtype: int
            """
            count = 0
            for row in grid:
                count += sum(1 for num in row if num < 0)
            return count
    # class Solution2:
        # def coun

    pr = Solution1().countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])
    print(pr)

# 2529. Maximum Count of Positive Integer and Negative Integer

if 0:
    class Solution:
        def maximumCount(self, nums: list) -> int:
            pos = 0
            neg = 0
            for el in nums:
                if el > 0:
                    pos += 1
                elif el < 0:
                    neg += 1
            return pos if pos > neg else neg
        
    class Solution:
        def maximumCount(self, nums: list) -> int:
            pos = sum(1 for el in nums if el > 0)  # Musbat sonlar soni
            neg = sum(1 for el in nums if el < 0)  # Manfiy sonlar soni
            return max(pos, neg)  # Ko'pgina sonni qaytaradi

            
    pr = Solution().maximumCount([-2, -1, -1, 1, 2, 3])
    print(pr)

