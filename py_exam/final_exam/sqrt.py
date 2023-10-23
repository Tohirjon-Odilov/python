def sqrt(n:int) -> int:
    if n < 0:
        return "Error"
    return n ** .5

print(sqrt(int(input(">>> "))))