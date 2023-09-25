sekund = int(input("Sekundlarni kiriting: "))
hour = sekund // 3600
sekund = sekund % 3600
minut = sekund // 60
sekund = sekund % 60
print(f"{hour} soat {minut} minut {sekund} sekunt")
