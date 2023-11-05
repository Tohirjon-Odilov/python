def maximum(a:int, b:int) -> int:
    return (a+b)//2 + abs(a-b)//2

print(maximum(int(input("a: ")), int(input("b: "))))