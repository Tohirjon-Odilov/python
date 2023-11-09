# def num_180(num:int) -> bool:
#     num = str(num)
#     res = str()
#     for el in num:
#         if el == "9":
#             res += "6"
#         elif el == "6":
#             res += "9"
#         elif el == '8':
#             res += "8"
#         elif el == '0':
#             res += "0"
#     return int(num) == int(res[::-1])
            
# print(num_180(609609))
# print(num_180(9669))
# print(num_180(69069069))

def nums(num: int) -> bool:
    num = str(num)
    for i in range(len(num)//2):
        if num[i] == "6" and num[len(num)-i-1] == "9" or num[i] == "9" and num[len(num)-i-1] == "6" or num[i] == "0" and num[len(num)-i-1] == "0" or num[i] == "8" and num[len(num)-i-1] == "8":
            return True
        else:
            return False

num = int(input())
print(nums(num))
