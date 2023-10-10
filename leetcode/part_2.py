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

# 744. Find Smallest Letter Greater Than Target
if 1:
    class Solution:
        def nextGreatestLetter(self, letters: list[str], target: str) -> str:
            new = letters
            new.append(target)
            new = list(set(new))
            new = sorted(new)
            try:
                x = new[new.index(target)+1]
            except IndexError:
                x = letters[0]
            return x
        
        
    print(Solution().nextGreatestLetter(["c","l","f"], "a"))
    print(Solution().nextGreatestLetter(["c","f","j"], "c"))
    print(Solution().nextGreatestLetter(["c","f","j"], "d"))


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

# 1572. Matrix Diagonal Sum
if 0:
    class Solution:
        def diagonalSum(self, mat: list[list[int]]) -> int:
            main, reverse, n = list(), list(), len(mat)
            for i in range(n):
                main.append(mat[i][i])
                if i == n-i-1:
                    continue
                reverse.append(mat[i][n-i-1])
            return sum(main) + sum(reverse)
                
        
    print(Solution().diagonalSum([[1,2,3],
                                [4,5,6],
                                [7,8,9]]))

# 2418. Sort the People
if 1:
    class Solution:
        def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
            lst = list()
            for i in range(len(heights)):
                lst.append([names[i], heights[i]])
            return list(map(lambda a: a[0],sorted(lst, key=lambda x: x[1], reverse=True)))
        
    print(Solution().sortPeople(["Mary","John","Emma"], heights = [180,165,170])) 

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

