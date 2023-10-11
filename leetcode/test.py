# 345. Reverse Vowels of a String
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = list('aeuioAEUIO')
        old = dict()
        for i, el in enumerate(s):
            if el in vowels:
                old[i] = el
                
        new = str()
        value = list(reversed(list(old.values())))
        dic = dict()
        for i, el in enumerate(old.keys()):
            dic[el]=value[i]

        for i, el in enumerate(s):        
            if i in dic.keys():
                new += dic[i]
            else:
                new += el
        
        return new
print(Solution().reverseVowels("leetcode")) # "leotcede"


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
        





