# # Sizning vazifangiz ushbu sanadan boshlab eng yaqin oldindagi 13-Juma sanasini aniqlang.

# import datetime

# def friday_13(date: str) -> str:
#     day, month, year = list(map(int, date.split(".")))
#     for i in range(12):
#         time = datetime.date(year, i+1, day)
#         time += datetime.timedelta(days=1)
#         print(time)
#         if time.weekday() == 4 and time.day == 13:
#             return time
#         year += 1
#     time = datetime.date(year, month, day)
#     print(time)

# print(friday_13("1.1.2023"))
# print(friday_13("28.10.2023"))
# # print(friday_13("01.10.2023"))

# from datetime import datetime, timedelta

# # Foydalanuvchi tomonidan kiritilgan sana
# input_date = datetime(2023, 10, 28)

# # 13 kun qo'shib olish
# thirteen_days = timedelta(days=13)
# result_date = input_date + thirteen_days

# # Agar 13-Juma san'ati maqbul bo'lmasa, keyingi Juma san'atini topish
# while result_date.weekday() != 4:
#     result_date += timedelta(days=1)

# # Sanani ko'rinishini o'zgartiramiz
# result_date = result_date.strftime("%d.%m.%Y")

# print(f"input = {input_date.strftime('%d.%m.%Y')}")
# print(f"output = {result_date}")

from datetime import datetime, timedelta

time = input(">>> ").split('.')
year = int(time[2])
month = int(time[1])
day = int(time[0])

input_date = datetime(year, month, day)

thirteen_days = timedelta(days=13)
result_date = input_date + thirteen_days

while result_date.weekday() != 4:
    result_date += timedelta(days=1)

result_date = result_date.strftime("%d.%m.%Y")

print(result_date)
