# R1:

# Foydalanuvchi butun son kiritadi. Shu sonning raqamlari sonini
# aniqlovchi funksiya tuzing

def calculateNum(num: int, count: int) -> int:
    """
    Kiritilgan sonning raqamlar sonini aniqlab beradi.
    """
    if num == 0:
        count += 1
        return count
    return calculateNum(num//10, count + 1)


print(calculateNum(545, 0))
# num = int(input("Son kiriting: "))
