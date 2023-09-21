if 0:
	class Solution:
		def reverseWords(self, s: str) -> str:
			str = s.split()
			str = " ".join(list(map(lambda a: a[::-1], str)))
			
			return str
				

	exp = Solution()
	print(exp.reverseWords("Let's take LeetCode contest"))

if 0:
	class Solution:
		def findNumbers(self, nums: list[int]) -> int:
			nums = list(filter(lambda a: not len(str(a)) % 2, nums))
			return len(nums)
	exp = Solution()
	print(exp.findNumbers([12, 1, 2, 345, 1234]))

if 0:
	class Solution(object):
		def reverseStr(self, s, k):
			a = list(s)
			for i in range(0, len(a), 2*k):
				a[i:i+k] = reversed(a[i:i+k])
			return "".join(a)
	exp = Solution()
	print(exp.reverseStr("abcdefg", 2))

if 0:
	class Solution:
		def areNumbersAscending(self, s: str) -> bool:
			s = s.split()
			lst = list()
			lst2 = list()
			for i in s:
				if i.isdigit():
					lst.append(int(i))
			for i in range(len(lst)):
				if lst[i-1] == lst[i]:
					return False
			if lst == sorted(lst):
				return True
			return False

	exp1 = Solution()
	print(exp1.areNumbersAscending("5, 5"))
	print(exp1.areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles"))
	print(exp1.areNumbersAscending("sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"))