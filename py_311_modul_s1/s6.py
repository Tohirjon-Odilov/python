# S6:

# Foydalanuvchi istlagan xonali son kiritadi va sizning vazifangiz ushbu
# sonni birliklar, o’nliklar, yuzliklar va hokazo xonalar yig’indisi
# yoyilmasiga aylantirib chiqaradigan funksiya tuzish. strga yig'ib
# qaytarsin.

# input: 123
# output: 100+20+3

# input: 4213
# output: 4000+200+10+3

def yigindi_yoyish(son):
    str_son = str(son)
    return "+".join([d + "0" * (len(str_son) - i - 1)
                     for i, d in enumerate(str_son)])


print(yigindi_yoyish(int(
    input("Istalgan xonali sonni kiriting: "))))
