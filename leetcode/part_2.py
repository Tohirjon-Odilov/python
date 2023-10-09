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
if 1:
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
            


