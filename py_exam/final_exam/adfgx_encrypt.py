def adfgx_encrypt(text: str, key: str) -> str:
    shifr = "ADFGX"
    shifr = dict(zip(key, [shifr[i]+shifr[j] for i in range(5) for j in range(5)]))
    return "".join([shifr[i] for i in text if i in shifr])

# print(adfgx_encrypt("helloworld", "bchigklnmoqprstuvwxyzadef"))
print(adfgx_encrypt(input(), input()))
