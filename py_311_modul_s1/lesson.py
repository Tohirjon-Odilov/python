# import platform

# x = platform.node()
# print(x)
# import platform

# x = dir(platform)
# print(x)

# import my_func

# print(dir(my_func))

#  x = 300

# def myfunc():
#   # global x
#   x = 200

# myfunc()

# print(x)
if 0:
    try:
        print(x)
    except Exception:
        print("An exception occurred")

if 1:
    try:
        f = open("demofile.txt")
        try:
            f.write("Lorum Ipsum")
        except Exception:
            print("Something went wrong when writing to the file")
        finally:
            f.close()
    except Exception:
        print("Something went wrong when opening the file")
