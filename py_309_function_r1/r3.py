# R3:

# a dan b gacha sonlarni ekranga chiqaradigan recursive function tuzing.
# Faqat, a >= b dan bo'lgan holatlar uchun

# Input:    7 2
# Output: 7 6 4 5 3 2

def rev(a: int, b: int):
    if a >= b:
        print(a)
        rev(a-1, b)


rev(7, 2)
