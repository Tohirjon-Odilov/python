class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def qoshish(self, other_fraction):
        jami_surat = self.numerator * other_fraction.denominator + other_fraction.numerator * self.denominator
        jami_maxraj = self.denominator * other_fraction.denominator
        return Fraction(jami_surat, jami_maxraj)

    def ayirish(self, other_fraction):
        jami_sanat = self.numerator * other_fraction.denominator - other_fraction.numerator * self.denominator
        jami_maxraj = self.denominator * other_fraction.denominator
        return Fraction(jami_sanat, jami_maxraj)

    def kopaytirish(self, other_fraction):
        jami_sanat = self.numerator * other_fraction.numerator
        jami_maxraj = self.denominator * other_fraction.denominator
        return Fraction(jami_sanat, jami_maxraj)

    def bolish(self, other_fraction):
        jami_sanat = self.numerator * other_fraction.denominator
        jami_maxraj = self.denominator * other_fraction.numerator
        return Fraction(jami_sanat, jami_maxraj)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


# Fraction obyektlarini yaratish
kasr1 = Fraction(int(input("Sur'at'ni kiriting: ")), int(input("Maxrajni kiriting: ")))
kasr2 = Fraction(int(input("Sur'at'ni kiriting: ")), int(input("Maxrajni kiriting: ")))

# Kasr sonlarini qo'shish
jami = kasr1.qoshish(kasr2)
print(f"Qo'shilgan kasr: {jami}")

# Kasr sonlarini ayiramiz
ayirma = kasr1.ayirish(kasr2)
print(f"Ayirilgan kasr: {ayirma}")

# Kasr sonlarini ko'paytirish
kopaytirish = kasr1.kopaytirish(kasr2)
print(f"Ko'paytirilgan kasr: {kopaytirish}")

# Kasr sonlarini bo'lish
bolish = kasr1.bolish(kasr2)
print(f"Bo'linuvchi kasr: {bolish}")
