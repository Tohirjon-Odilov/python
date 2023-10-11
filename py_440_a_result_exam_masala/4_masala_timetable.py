# 
class Time:
    def __init__(self, hour, minut, sekund) -> None:
        self.hour = hour
        self.minut = minut
        self.sekund = sekund
    def __repr__(self) -> str:
        return f"{self.hour}:{self.minut}:{self.sekund}"
    
class TimeTable(Time):
    def __init__(self, hour, minut, sekund, subject, start_time, classroom) -> None:
        super().__init__(hour, minut, sekund)
        self.subject = subject
        self.start_time = start_time
        self.classroom = classroom

subject1 = TimeTable(hour=9, minut=30, sekund=0, subject='Math', start_time='8:30', classroom='A101')
subject2 = TimeTable(hour=9, minut=45, sekund=0, subject='Physics', start_time='8:45', classroom='A102')
subject3 = TimeTable(hour=10, minut=0, sekund=0, subject='Chemistry', start_time='9:00', classroom='A103')
subject4 = TimeTable(hour=10, minut=15, sekund=0, subject='Biology', start_time='9:15', classroom='A104')
subject5 = TimeTable(hour=10, minut=30, sekund=0, subject='English', start_time='9:30', classroom='A105')

def bilmadim():
    print(subject1)