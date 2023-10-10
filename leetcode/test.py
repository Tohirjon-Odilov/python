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
        
