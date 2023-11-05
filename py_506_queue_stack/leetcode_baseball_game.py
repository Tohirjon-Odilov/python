from click import clear


clear()

class Solution:
    def calPoints(self, operations: list[str]) -> int:
        nums = list()
        for i in operations:
            if i == "C":
                nums = nums[:-1]
            elif i == "D":
                nums.append(nums[-1] * 2)
            elif i == "+":
                nums.append(nums[-1] + nums[-2])
            else:
                nums.append(int(i))

        return sum(nums)
    
print(Solution().calPoints(["5","-2","4","C","D","9","+","+"]))