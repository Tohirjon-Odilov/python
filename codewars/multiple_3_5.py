# def solution(number):
#     s = 0
#     for i in range(3, number):
#         if i % 3 == 0 or i % 5 == 0:
#             s += i
#     return s
#


def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)


print(solution(16))
