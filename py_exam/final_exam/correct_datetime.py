import datetime

def correct_date_time(day, month, year, hour, minute) -> bool:
    try:
        vaqt = datetime.datetime(year, month, day)
        vaqt += datetime.timedelta(hour, minute)
    except:
        return False
    return True

print(correct_date_time(12,12,2023,15,58))
print(correct_date_time(78,12,2023,25,68))
print(correct_date_time(7, "Yanvar", "2023-yil", 10,00))
