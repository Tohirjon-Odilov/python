# def pharmacy()
# for i in range(1,9):
    # print(str(i).center(i*4, " "))
# for i in range(9,0,-1):
    # print(str(i).center(i*4, " "))
    
def rec(num, b):
    if num == 0:
        print("0")
        return b
    
    print(str(num).center(num*5, " "))
    n = 50
    print(str(num).center(n, " "))
    rec(num-1, b+str(num))
    # n = 50
    print(str(num).center(n, " "))
    print(str(num).center(num*5, " "))
    
rec(10, '1')