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
 
#  344. Reverse String
if 0:
    class Solution:
        def reverseString(self, s: list[str]) -> None:
            """
            Do not return anything, modify s in-place instead.
            """
            s.reverse()
            return s
        
    print(Solution().reverseString(["h","e","l","l","o"]))
 
# 349. Intersection of Two Arrays
if 0:
    class Solution:
        def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
            return list(set(nums1).intersection(set(nums2)))
    
    pr = Solution().intersection([1,2,2,1],[2,2])
    print(pr)           

# 350. Intersection of Two Arrays II
if 1:
    class Solution:
        def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
            i,j = 0, 0
            result = list()
            nums1, nums2 = sorted(nums1), sorted(nums2)

            while i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    i += 1
                elif nums1[i] > nums2[j]:
                    j += 1
                else:
                    result.append(nums1[i])
                    j += 1
                    i += 1
            return result
    
    print(Solution().intersect([1,2,2,1], [2,2]))
    
# 744. Find Smallest Letter Greater Than Target
if 0:
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

# 896. Monotonic Array
if 0:
    class Solution:
        def isMonotonic(self, nums: list[int]) -> bool:
            return True if nums == list(sorted(nums)) or list(sorted(nums))[::-1] == nums else False
        
    print(Solution().isMonotonic([1,2,2,3]))
    print(Solution().isMonotonic([6,5,4,4]))
    print(Solution().isMonotonic([6,3,4,2]))

# 1122. Relative Sort Array
if 0:
    class Solution:
        def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
            res = list()
            for i in range(len(arr2)):
                for j in range(len(arr1)):
                    if arr2[i] == arr1[j]:
                        res.append(arr1[j])
            arr1.sort()
            l = list()
            for i in range(len(arr1)):
                if not arr1[i] in res:
                    l.append(arr1[i])

            return res+l
            
    
    print(Solution().relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))
    # [2,2,2,1,4,3,3,9,6,7,19]

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

# 1480. Running Sum of 1d Array
if 0:
    class Solution:
        def runningSum(self, nums: list[int]) -> list[int]:
            sum = [nums[0]]
            for i in range(1, len(nums)):
                sum.append(sum[-1]+nums[i])
            return sum
                        
    print(Solution().runningSum([1,2,3,4])) # [1,3,6,10]

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

# 1816. Truncate Sentence
if 0:
    class Solution:
        def truncateSentence(self, s: str, k: int) -> str:
            s = s.split()
            return s if len(s) < k else " ".join(s[:k])
    
    print(Solution().truncateSentence("Hello how are you Contestant", 4)) #"Hello how are you"

# 2164. Sort Even and Odd Indices Independently
if 0:
    class Solution:
        def sortEvenOdd(self, nums: list[int]) -> list[int]:
            odd, even, res = list(), list(), list()
            for i, el in enumerate(nums, 1):
                if i % 2 == 0:
                    even.append(el)
                else:
                    odd.append(el)
            odd.sort()
            even.sort(reverse=True)
                          
            try:
                for i, el in enumerate(odd, 1):
                    res.append(el)
                    res.append(even[i])
            except:
                res.append(odd.pop())
                    
            return res
        
    print(Solution().sortEvenOdd([4,1,2,3])) #[2,3,4,1]
    print(Solution().sortEvenOdd([2,1])) #[2,1]
    print(Solution().sortEvenOdd([5,39,33,5,12,27,20,45,14,25,32,33,30,30,9,14,44,15,21]))

# 2418. Sort the People
if 0:
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

# 2574. Left and Right Sum Differences
if 0:
    class Solution:
        def leftRightDifference(self, nums: list[int]) -> list[int]:
            rigthsum = sum(nums)
            leftsum = 0
            result = list()
            for i in nums:
                result.append(abs(rigthsum - leftsum - i))
                rigthsum -= i
                leftsum += i
            return result
        
    print(Solution().leftRightDifference([10,4,8,3]))
