# S5:

# Funksiya orqali Stringga bir nechta so'z va gaplar berilgan. Ushbu
# stringdagi ma'lumotlarni so'zlarni va gaplarni alohida listlarga
# joylashtiradigan funksiya tuzing.
# Input: Salom Yoz. Olam juda ham go’zal. Imtihon bo’lyapti.
# Output:
# words: [Salom, Yoz, Olam, juda, ham, go’zal, Imtihon, bo’lyapti]
# sentence: [Salom Yoz, Olam juda ham go’zal, Imtihon bo’lyapti]

txt = "Salom Yoz. Olam juda ham go’zal. Imtihon bo’lyapti."
words = list(map(lambda a: a.replace(".", ''), txt.split()))
sentence = list(filter(lambda a: len(a) != 0, txt.split(".")))
print("words:", words)
print("sentence:", sentence)
