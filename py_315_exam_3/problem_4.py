""""
Fayl ichiga input orqali katta butun son yoziladi va ushbu sonni sekund deb tasavvur qiladigan
bo'lsak, ushbu sekundni kun, soat, minut va sekundga ajratib chiqarib bering.
"""
with open("file.txt", "w") as f:
    f.write(input())

with open("file.txt", "r") as f:
    seconds = int(f.read())
    day = seconds // (24 * 3600)
    seconds %= 24 * 3600
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    print(f"kun: {day}, soat: {hour}, minut: {minutes}, sekund: {seconds}.")
