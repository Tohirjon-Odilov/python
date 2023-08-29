def persistence(n):
    count = 0
    while n:
        n = str(n)
        if len(n) == 1:
            break
        n = int(n[0]) * int(n[1])
        count += 1
    return count


print(persistence(999))
