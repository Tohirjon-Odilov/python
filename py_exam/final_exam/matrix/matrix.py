def matrix(n:int) -> list:
    try:
        with open("./matrix/matrix.txt", "w") as file:
            for i in range(n):
                for j in range(n):
                    if i == j or i+j == n-1:
                        file.write("1 ")
                        continue
                    file.write("0 ")
                file.write("\n")
    except:
        print("Papka topilmadi!")
    else:
        print("Success.")

matrix(int(input(">>> ")))
