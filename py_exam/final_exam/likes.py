def txt(texts: list) -> str:
        if texts != []:
            words = str()
            text_len = len(texts)
            for i in range(text_len):
                if text_len < 2:
                    words += texts[i]
                elif i != text_len - 1:
                    words += texts[i]+", "
                else:
                    words = words[:-2]+" and "+texts[i]
            return words + " likes this"
        else:
            return "no one likes this"

print(txt(input("Enter: ").split()))