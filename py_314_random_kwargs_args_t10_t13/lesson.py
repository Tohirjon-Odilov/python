# with("../py_312_file_t1/booking_data.txt", "r") as f:
#     print("slaom")
# file1 = open("test1.txt", "x")
# file1.close()
if 0:
    with open("test.txt", "r") as f:
        # print(f.write("salom dunyoda nima gaplar olamdachi"))
        # print(f.read())
        # print(f.fileno())
        # f.flush()
        print(f.seek(10))
        print(f.read())
# f = open("test.txt", "a")
# f.write("Now the file has one more line!")
# f.flush()
# f.write("...and another one!")
# print(detach(f))
# file = open("test.txt", "r")
# print(file.read())
if 0:
    f = open("test.txt", "a")
    f.truncate(20)
    f.close()

    # open and read the file after the truncate:
    f = open("test.txt", "r")
    print(f.read())
if 1:
    import random

    # print(random.random())
    # state = random.getstate()
    # print(random.random())
    # random.setstate(state)
    # print(random.random())
    # print(random.random())

    # print(random.getrandbits(8))
    # for i in range(100):
    #     print(random.randrange(3, 10, 5), end=" ")
    # print(random.randint(3, 9), end=" ")
    # x = "WELCOME"

    # print(random.choice("tasodif"))

    mylist = ["apple", "banana", "cherry"]
    # print(random.choices(mylist, weights=[10, 1, 2], k=14))
    # print(random.sample(mylist, k=12))
    # for i in range(100):
    print(random.betavariate(beta=10, alpha=10))
