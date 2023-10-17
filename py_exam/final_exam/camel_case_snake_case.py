def to_case(text:str):    
    text = list(text)
    camel = list()
    
    for i in range(len(text)):
        try:
            if text[i] == "_":
                text.pop(i)
                text[i] = text[i].upper()
            else:
                if text[i].isupper():
                    camel.append("_" + text[i].lower())
                else:
                    camel.append(text[i])
        except:
            return "".join(text)
            
    return "".join(camel)


print(to_case("hello_code_chick"))
print(to_case("helloCodeChick"))
print(to_case("is_modal_open"))
print(to_case("getColor"))