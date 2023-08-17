num = int(input())

summa = 0

if num <= 0:
    for i in range(1, num-1, -1):
        summa += sum([i])
else:
    for i in range(num + 1):
        summa += sum([i])

print(summa)
