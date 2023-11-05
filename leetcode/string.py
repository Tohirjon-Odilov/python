# 9. Palindrome Number
if 0:
    class Solution:
        def isPalindrome(self, x: int) -> bool:
            x = str(x)
            return x == x[::-1]
        
    print(Solution().isPalindrome(121)) #True
    
# 13. Roman to Integer
if 1:
    class Solution:
        def romanToInt(self, s: str) -> int:
            romans = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000
            }
            result, prev_value = 0, 0
            for i in s[::-1]:
                value = romans[i]
                if prev_value > value: # 5 - 1
                    print(f"{prev_value}-{value}={prev_value-value}")
                    result -= value
                else:
                    print(f"{prev_value}+{value}={prev_value+value}")
                    result += value
                prev_value = value
            return result
    
    print(Solution().romanToInt("MCMXCIV")) # 1994
    print(Solution().romanToInt("LVIII")) # 58

# 28. Find the Index of the First Occurrence in a String
if 0:
    class Solution:
        def strStr(self, haystack: str, needle: str) -> int:
            return haystack.find(needle)

    print(Solution().strStr("hello", "ll")) #2
    print(Solution().strStr("aaaaa", "bba")) #-1
    print(Solution().strStr("mississippi", "issip")) #4.

# 1108. Defanging an IP Address
if 1:
    class Solution:
        def defangIPaddr(self, address: str) -> str:
            # res = list()
            # for i in address:
            #     if i == ".":
            #         res.append("[.]")
            #     else:
            #         res.append(i)
            # return "".join(res)
            
            # address = list(address)
            # for i in range(len(address)):
            #     if address[i] == ".":
            #         address.pop(i)
            #         address.insert(i,"[.]")
            # return "".join(address)
            
            return address.replace(".", "[.]")
        
    print(Solution().defangIPaddr("1.1.1.1"))