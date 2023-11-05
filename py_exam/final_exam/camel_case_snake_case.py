# def to_case(text:str):    
#     text = list(text)
#     camel = list()
    
#     for i in range(len(text)):
#         try:
#             if text[i] == "_":
#                 text.pop(i)
#                 text[i] = text[i].upper()
#             else:
#                 if text[i].isupper():
#                     camel.append("_" + text[i].lower())
#                 else:
#                     camel.append(text[i])
#         except:
#             return "".join(text)
            
#     return "".join(camel)

# print(to_case("hello_code_chick"))
# print(to_case("helloCodeChick"))
# print(to_case("is_modal_open"))
# print(to_case("getColor"))

def to_case(word: str):
    new_word = str()
    for i in range(len(word)):
        if word[i].isupper():
            new_word += "_" + word[i].lower()
        elif word[i-1] == "_":
            new_word += word[i].upper()
        elif word[i].isalnum():
            new_word += word[i]
    return new_word

# print(to_case(input(">>> ")))

# print(to_case("hello_code_chick"))
# print(to_case("helloCodeChick"))
print(to_case("is_modal_open"))
print(to_case("getColor"))