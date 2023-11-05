def c_format(text: str) -> str:
    text = text.split("\n")
    new_text = str()
    for el in text:
        if el.find("+1") != -1:
            j = len(el) - len(el.strip())
            new_text += f"{' ' * j}{el.strip()[0]}++;"
        else:
            new_text += el
        new_text += "\n"
    return new_text[:-1]

print(c_format("""#include<stdio.h>
int main()
{
    int a=5;
    a=a+1;
    int b=a*a;
    b=b+1;
    printf("a=%d\\tb=%d\\n", a,b);
    return 0;
}"""))
