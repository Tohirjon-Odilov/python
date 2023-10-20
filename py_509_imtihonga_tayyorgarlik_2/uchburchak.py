def triangle(a: str, b: str) -> bool:
    a = list(map(sum, eval(a)))
    aa = a[0]
    for i in a:
        aa = abs(aa-i)
    print(aa)
    b = list(map(sum, eval(b)))

    return a,b

print(triangle("[(0,0), (1,2), (2,0)]", "[(3,0), (4,2), (5,0)]"))
print(triangle("[(0,0), (1,2), (2,0)]", "[(3,0), (4,3), (5,0)]"))
print(triangle("[(1,0), (1,2), (2,0)]", "[(3,0), (5,4), (5,0)]"))
print(triangle("[(0,0), (1,2), (2,0)]", "[(3,0), (4,2), (4,0)]"))