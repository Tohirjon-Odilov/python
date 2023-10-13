# 2. Add Two Numbers
if 0:
    class Solution:
        def addTwoNumbers(self, l1, l2):
            return list(map(int, list(str(int("".join(map(str, l1)))+int("".join(map(str, l2)))))[::-1]))
            
    print(Solution().addTwoNumbers([2,4,3],[5,6,4]))  

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