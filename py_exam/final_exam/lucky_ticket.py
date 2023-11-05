# def ticket(num: int)->int:
#     if num % 2:
#         return "ERROR"
#     count = int()
#     n = int("1"+"0"*(num-1))
#     # print(n)
#     # return
#     for i in range(n):
#         j = str(("0"*(num-1))+str(i))
#         # print(j)
#         if eval("+".join(list(j[:len(j)//2]))) == eval("+".join(list(j[len(j)//2:]))):
#             count += 1
#         print(j)
#     # return count
#     for i in range(n, int("9"*num)+1):
#         i = str(i)
#         # if len(i) == 2:
            
#         if eval("+".join(list(i[:len(i)//2]))) == eval("+".join(list(i[len(i)//2:]))):
#             # eval("+".join(list(i[:len(i)//2])))
#             # print(list(i[:len(i)//2]), list(i[len(i)//2:]))
#             # print((eval("+".join(list(i[:len(i)//2]))),eval("+".join(list(i[len(i)//2:])))))
#             count += 1
#             # print(count)

#         # print(i)
#         # num_len = len(str(i))
#         # if str(i)[:num_len//2] == str(i)[num_len//2:]:
#         #     count += 1
#     return count

# # print(ticket(2))
# print(ticket(4))
# # print(ticket(12))
# # 02 11


def lucky_ticket(num):
    num2 = str(0)*num
    # print(num2)
    counter = 0
    while len(num2) < num+1:
        a = sum(list(map(int, list(num2[0:len(num2)//2]))))
        # print(a)
        b = sum(list(map(int, list(num2[len(num2)//2:len(num2)]))))
        print(a,b)
        if a != b:
            num2 = int(num2)+1
            continue
        if a == b:
            counter += 1
        # print(num2)
        num2 = int(num2)+1
        # print(num2)
        num2 = (num - len(str(num2))) * '0' + str(num2)
        # print(num2)
    return counter
        
        



n = int(input('n = '))
print(lucky_ticket(n))