from click import clear


clear()

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
                if prev_value > value:
                    print(f"{prev_value}-{value}={prev_value-value}")
                    result -= value
                else:
                    print(f"{prev_value}+{value}={prev_value+value}")
                    result += value
                prev_value = value
            return result
    
    print(Solution().romanToInt("MCMXCIV")) # 1994
    print(Solution().romanToInt("LVIII")) # 58
        
















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
        










