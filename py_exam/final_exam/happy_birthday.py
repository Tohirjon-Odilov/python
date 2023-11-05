def birthday(name, age):
    char = str("*" if int(age) % 2 else "#")
    text = f"{char} {age} Happy Birthday {name}! {age} {char}"
    char = char*len(text)
    return f"""{char}\n{text}\n{char}"""
    
print(birthday(input("Enter name: "), input("Enter age: ")))