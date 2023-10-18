def fibonacci_piramida(N):
    a, b, count, idx = 0, 1, 0, 0

    for i in range(N):
        if count+i < N: 
            idx, count = idx + 1, count + i 
        else: break

    count = 0
    for i in range(idx):
        for _ in range(N - i - 1):
            print(" ", end="")
        for _ in range(i + 1):
            if count < N:
                print(f"{b} ", end="")
                a, b, count = b, a + b, count + 1
            else:
                break
        print("")

fibonacci_piramida(int(input("N = ")))
