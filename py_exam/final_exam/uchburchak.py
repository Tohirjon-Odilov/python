# def triangle(a: str, b: str) -> bool:
#     a = list(map(sum, eval(a)))
#     aa = a[0]
#     for i in a:
#         aa = abs(aa-i)
#     print(aa)
#     b = list(map(sum, eval(b)))

#     return a,b

# def triangle(uchburchak1, uchburchak2):
#     uchburchak1 = eval(uchburchak1)
#     uchburchak2 = eval(uchburchak2)
#     print(set(uchburchak1),set(uchburchak2))
    
#     if set(uchburchak1) == set(uchburchak2):
#         return "Uchburchaklar o'xshash"
#     else:
#         return "Uchburchaklar bir xil emas"

def triangle(a,b):
    # a = [[0,0], [1,2], [2,0]]
    # b = [[1,0], [1,2], [2,0]]
    bool1 = False
    bool2 = False

    if a[0][0] == a[1][0] or a[0][0] == a[2][0] or a[1][0] == a[2][0]:
        bool1 = True
    else:
        bool1 = False
        
    if b[0][0] == b[1][0] or b[0][0] == b[2][0] or b[1][0] == b[2][0]:
        bool2 = True
    else:
        bool2 = False
        
    if bool1 == bool2:
        return True
    elif bool1 != bool2:
        return False


print(triangle("[(0,0), (1,2), (2,0)]", "[(3,0), (4,2), (5,0)]"))
print(triangle("[(0,0), (1,2), (2,0)]", "[(3,0), (4,3), (5,0)]"))
print(triangle("[(1,0), (1,2), (2,0)]", "[(3,0), (5,4), (5,0)]"))
print(triangle("[(0,0), (1,2), (2,0)]", "[(3,0), (4,2), (4,0)]"))