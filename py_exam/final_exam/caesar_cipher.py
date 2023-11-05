# def caesar_cipher(text, key):
#     res = str()
#     text = text.upper()
#     for i in text:
#         num = ord(i)
#         if 65 <= num+key <= 90:
#             res += chr((num+key))
#         elif num == 32:
#             res += " "
#         else:
#             res += chr((num+key)%91+65)
#     return res.lower()

# print(caesar_cipher("hello", 5))
# print(caesar_cipher("hello world", 1))
# print(caesar_cipher("xyz", 2))

def caesar_cipher(text, key):
    retstr = ""
    lst = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for i in text:
        if i == " ":
            retstr += " "
            continue
        
        i = i.upper()
        if i in lst:
            char = lst.index(i)
            retstr += lst[(char+key)%len(lst)]
            
    return retstr.lower()
    
print(caesar_cipher("hello", 5))
print(caesar_cipher("hello world", 1))
print(caesar_cipher("z", 2))
    