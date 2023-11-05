import datetime

def friday_of_13(year):
    count = 0
    for month in range(1, 13):
        if datetime.date(year, month, 13).weekday() == 4:
            count += 1
    return count

print(friday_of_13(int(input(">>> "))))
