from datetime import datetime

class Aeroport:
    def __init__(self, name, location, clientCapacity, 
                 clientCount, capital, establishedAt) -> None:
        self.name = name
        self.location = location
        self.clientCapacity = clientCapacity
        self.clientCount = clientCount
        self.capital = capital
        self.establishedAt = establishedAt
    
    def remainPlace(self):
        return self.clientCapacity - self.clientCount

    def created(self):
        date = datetime.strptime(self.establishedAt, "%Y/%m/%d %H:%M:%S")
        time = datetime.now() - date
        year = time.days//365
        month = time.days%365//31
        day = time.days%365%31
        print(f"{year} year, {month} month, {day} day, {time}")
    
# aer1 = Aeroport('Москва', 'Москва', 100, 50, 1000000, "2020/10/20 10:20:50")
# aer2 = Aeroport('Москва', 'Москва', 100, 50, 1000000, "2010/10/20 10:20:50")
# aer3 = Aeroport('Москва', 'Москва', 100, 50, 1000000, "2022/10/20 10:20:50")
# aer4 = Aeroport('Москва', 'Москва', 100, 50, 1000000, "2021/10/20 10:20:50")
# aer5 = Aeroport('Москва', 'Москва', 100, 50, 1000000, "2012/10/20 10:20:50")

# aer2.created()

