# 2. Add Two Numbers
if 0:
    class Solution:
        def addTwoNumbers(self, l1, l2):
            return list(map(int, list(str(int("".join(map(str, l1)))+int("".join(map(str, l2)))))[::-1]))
            
    print(Solution().addTwoNumbers([2,4,3],[5,6,4]))  

# 14. Longest Common Prefix
if 1:
    class Solution:
        def longestCommonPrefix(self, strs: list[str]) -> str:
            comman=""
            # returning "" , if  List is not present 
            if len(strs)==0:
                return comman

            # 0 to first_string length
            for i in range(len(strs[0])):
                print(i)
                for s in strs:
                    if i==len(s) or s[i]!=strs[0][i]:
                        print(s[i])
                        return comman
                comman+=strs[0][i]
            return comman
        
    print(Solution().longestCommonPrefix(["flower","flow","flight"])) #fl
    

# 27. Remove Element
if 1:
    class Solution:
        def removeElement(self, nums: list[int], val: int) -> int:
            while val in nums:
                nums.remove(val)
            return len(nums)
        
    print(Solution().removeElement([3,2,2,3], 3)) #[2,2,_,_]

# 66. Plus One
if 0:
    class Solution:
        def plusOne(self, digits: list[int]) -> list[int]:
            return list(map(int, list(str(int("".join(map(str, digits)))+1))))
            
print(Solution().plusOne([1,2,3])) # [1,2,4]

# 2011. Final Value of Variable After Performing Operations
if 0:
    class Solution:
        def finalValueAfterOperations(self, operations: list[str]) -> int:
            res = 0
            for i in operations:
                if i == "++X" or i == "X++":
                    res += 1
                elif i == "--X" or i == "X--":
                    res -= 1
            return res
            

    print(Solution().finalValueAfterOperations(["X++","++X","--X","X++"])) # 2