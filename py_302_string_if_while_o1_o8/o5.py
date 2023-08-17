i, count = 0, 2

while i <= 1000:
    count = 0
    j = 2
    while j <= i//2:
        if (i % j) == 0:
            count += 1
        j += 1
    if count == 7:
        print(i, end=" ")
    i += 1
