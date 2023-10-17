class Time:
    def __init__(self) -> None:
        self.time = input("Enter time: ").split(":")
        self.hour = self.time[0]
        self.minut = self.time[1]
        self.second = self.time[2]
        
class TimeTable(Time):
    def __init__(self, subject, start_time, classroom) -> None:
        super().__init__()
        self.time = f"{self.hour}:{self.minut}:{self.second}"
        self.subject = subject
        self.start_time = start_time
        self.classroom = classroom
        self.fit_time()
    
    def fit_time(self):
        if self.time == self.start_time:
            print(self.get_info())
        else:
            print("Empty")

    def get_info(self) -> str:
        return f"Subject: {self.subject}\nStart time: {self.start_time}\nClassroom: {self.classroom}\n"
    
cl1 = TimeTable("Rus til", "08:30:00", "B101")
cl2 = TimeTable("Ingiliz til", "10:30:00", "A202")
cl3 = TimeTable("Adabiyot", "11:00:00", "C120")
cl4 = TimeTable("Informatika", "11:00:00", "B103")
cl5 = TimeTable("Ona tili", "12:30:00", "L203")

    