# O3:

# 1 +11 + 111 + 1111 + .. n hadlar qatorining yig'indisini topish dasturini
# yozing.
# Test:
# n= 5
# Kutilayotgan natija:
# 1 + 11 + 111 + 1111 + 11111
# Sum: 12345

n = int(input("N = "))

summa = 0

for i in range(1, n+1):
    summa += int("1" * i)
    if i == n:
        print("1" * i, end=" = ")
    else:
        print("1" * i, end=" + ")
print(summa)
