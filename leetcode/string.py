# 28. Find the Index of the First Occurrence in a String
if 1:
    class Solution:
        def strStr(self, haystack: str, needle: str) -> int:
            return haystack.find(needle)

    print(Solution().strStr("hello", "ll")) #2
    print(Solution().strStr("aaaaa", "bba")) #-1
    print(Solution().strStr("mississippi", "issip")) #4
