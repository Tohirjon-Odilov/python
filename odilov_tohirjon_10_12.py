# y18
from click import clear


if 0:
    clear()
    def next_larger_number(n):
        digits = list(str(n))
        i = len(digits) - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1

        if i == -1:
            return -1

        j = len(digits) - 1
        while digits[j] <= digits[i]:
            j -= 1

        digits[i], digits[j] = digits[j], digits[i]

        digits[i + 1:] = reversed(digits[i + 1:])

        result = int(''.join(digits))

        return result

    nums = input().split()
    nums = list(map(int, nums))
    for number in nums:
        print(next_larger_number(number))

# y19
if 0:
    clear()
    def fibonacci_piramida(N):
        a, b, count, idx = 0, 1, 0, 0

        for i in range(N):
            if count+i < N: 
                idx, count = idx + 1, count + i 
            else: break

        count = 0
        for i in range(idx):
            for _ in range(N - i - 1):
                print(" ", end="")
            for _ in range(i + 1):
                if count < N:
                    print(f"{b} ", end="")
                    a, b, count = b, a + b, count + 1
                else:
                    break
            print("")

    fibonacci_piramida(int(input("N = ")))

# y20
if 0:
    clear()
    def txt(texts: list) -> str:
        if texts != []:
            words = str()
            text_len = len(texts)
            for i in range(text_len):
                if text_len < 2:
                    words += texts[i]
                elif i != text_len - 1:
                    words += texts[i]+", "
                else:
                    words = words[:-2]+" and "+texts[i]
            return words + " likes this"
        else:
            return "no one likes this"

    print(txt(input("Enter: ").split()))

# y21
if 0:
    clear()
    def the_max_minus(nums: list):
        max_minus, idx = nums[0]-nums[1], [0, 1]
        for i in range(2, len(nums)-1):
            if max_minus < nums[i+1]-nums[i]:
                max_minus, idx = nums[i+1]-nums[i], [i, i+1]
        return max_minus, idx

    nums = list(map(int, input("N = ").split()))
    minus, ind = the_max_minus(nums)
    print(f"{minus}({nums[ind[0]]} va {nums[ind[1]]})")
