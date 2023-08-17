i = 1
print("Do'stona sonlar: ")
while i < 50000:
    j = 1
    summa_one = 0
    while j <= i//2:  # i = 220
        if i % j == 0:
            summa_one += j  # summa_one = 284
        j += 1

    j = 1
    summa_two = 0
    while j <= summa_one//2:
        if summa_one % j == 0:
            summa_two += j
        j += 1

    if summa_two == i and summa_two != summa_one and summa_one < summa_two:
        print(f"{summa_one} <---> {summa_two}")
    i += 1

# boshqa variant

# def sum_of_divisors(n):
#     divisors = [1]
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             divisors.append(i)
#             if i != n // i:
#                 divisors.append(n // i)
#     return sum(divisors)

# amicable_numbers = []

# for a in range(2, 50000):
    # b = sum_of_divisors(a)
    # if a != b and sum_of_divisors(b) == a and a < b and b < 50000:
        # amicable_numbers.append((a, b))
        # print(a,b)

# print("Barcha do'stona sonlar:")
# for pair in amicable_numbers:
    # print(pair)
