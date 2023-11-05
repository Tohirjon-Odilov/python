from datetime import datetime

def get_days(date1:list, date2: list)->int:
    try:
        date = datetime(date2[0], date2[1], date2[2]) - datetime(date1[0], date1[1], date1[2])
        return date.days
    except:
        return "Noto'g'ri sana kiritildi!"

print(get_days([2019, 6, 14], [2019, 6, 20]))
# print(get_days([2018, 12, 29], [2019, 1, 1]))
# print(get_days([2020, 5, 24], [2019, 5, 24]))

# print(get_days(list(map(int, input("Date 1=").strip().split(" "))), list(map(int, input("date 2=").strip().split(" ")))))