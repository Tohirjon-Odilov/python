from click import clear


clear()

if 1:
    class Solution:
        def uniqueMorseRepresentations(self, words: list[str]) -> int:
            # potential questions
                # can we expect all lower case
                # can we expect empty words dict
                # will the input be valid? non-numeric?
            converter = [
                ".-","-...","-.-.","-..",".","..-.","--.",
                "....","..",".---","-.-",".-..","--","-.",
                "---",".--.","--.-",".-.","...","-","..-",
                "...-",".--","-..-","-.--","--.."
            ]
            distinct = set()
            memo = {}
            def gen_code(word):
                if word in memo:
                    return memo[word]
                if not word: return ""
                return converter[ord(word[0])-ord('a')] + gen_code(word[1:])
                
            for word in words:
                distinct.add(gen_code(word))
            return len(distinct)
        
    print(Solution().uniqueMorseRepresentations(["gin","zen","gig","msg"]))

        

        
















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
        










