# 9. Palindrome Number
if 0:
    class Solution:
        def isPalindrome(self, x: int) -> bool:
            x = str(x)
            return x == x[::-1]
        
    print(Solution().isPalindrome(121)) #True

# 28. Find the Index of the First Occurrence in a String
if 0:
    class Solution:
        def strStr(self, haystack: str, needle: str) -> int:
            return haystack.find(needle)

    print(Solution().strStr("hello", "ll")) #2
    print(Solution().strStr("aaaaa", "bba")) #-1
    print(Solution().strStr("mississippi", "issip")) #4.
    

